import os
import re
import threading
from enum import Enum
from typing import Optional, Union, List, AnyStr
from urllib.parse import urlparse, urljoin

import click
import urllib3

from .base_client import BaseServiceClient
from ..auth import OAuthTokenAuth
from ..constants import DEFAULT_SERVICE_REGISTRY
from ..exceptions import DRSDownloadException, DRSException


class DRSObject:
    """
    A class for a DRS resource

    :param url: The DRS url
    :raises ValueError if url is not a valid DRS url
    """

    __RE_VALID_DRS_OBJECT_ID = re.compile(r'^[^/#?]+$')

    def __init__(self, url: str):
        try:
            DRSObject.assert_valid_drs_url(url)
        except AssertionError:
            raise ValueError("The provided url is not a valid DRS url")

        self.__url = url

    @property
    def url(self):
        return self.__url

    @property
    def object_id(self) -> str:
        """
        Return the object ID from a drs url

        :param url: A drs url
        :return: The object ID extracted from the URL
        :raises: ValueError if there isn't a valid DRS Object ID
        """
        parsed_url = urlparse(self.url)
        return parsed_url.path.split("/")[-1]

    @property
    def drs_server_url(self) -> str:
        """
        Return the HTTPS server associated with the DRS url

        :param url: A drs url
        :return: The associated HTTPS server url
        """
        parsed_url = urlparse(self.url)
        return urljoin(f'https://{parsed_url.netloc}{"/".join(parsed_url.path.split("/")[:-1])}', 'ga4gh/drs/v1/')

    @staticmethod
    def assert_valid_drs_url(url: str):
        """Returns true if url is a valid DRS url"""
        parsed_url = urlparse(url)
        assert parsed_url.scheme == r'drs', f'The scheme of the given URL ({url}) is invalid.'
        assert len(parsed_url.path) > 2 and parsed_url.path.startswith(r'/'), f'The ID is not specified in the URL ({url}).'
        assert DRSObject.__RE_VALID_DRS_OBJECT_ID.search(parsed_url.path[1:]), f'The format of the ID ({parsed_url.path[1:]}) is not valid.'


def handle_file_response(download_file: str, data: Union[str, bytes]) -> str:
    # decode if fasta
    if re.search(r"\.fa", download_file):
        data = data.decode("utf-8")

    return data


# turn into dataframe for FASTA/FASTQ files, otherwise just return raw data
def file_to_dataframe(download_file: str, data: Union[str, bytes]):
    if re.search(r"\.fa", download_file):
        data = data.split("\n", maxsplit=1)

        meta = data[0]
        sequence = data[1].replace("\n", "")  # remove newlines

        return pd.DataFrame({"meta": [meta], "sequence": [sequence]})

    return data


def get_filename_from_url(url: str) -> str:
    parsed_url = urlparse(url)
    return parsed_url.path.split("/")[-1]


class DownloadStatus(Enum):
    """An Enum to Describe the current status of a DRS download"""

    SUCCESS = 0
    FAIL = 1


class FilesClient(BaseServiceClient):
    def __init__(
        self,
        auth: Optional[OAuthTokenAuth] = None,
        registry_url: AnyStr = DEFAULT_SERVICE_REGISTRY,
    ):

        # A lock to prevent race conditions on exit_codes objects
        self.__output_lock = threading.Lock()
        # lock to prevent race conditions for file output
        self.__exit_code_lock = threading.Lock()

        super().__init__(auth=auth, registry_url=registry_url)

    def exit_download(
        self,
        url: str,
        status: DownloadStatus,
        message: str = "",
        exit_codes: dict = None,
    ) -> None:
        """
        Report a file download with a status and message

        :param url: The downloaded resource's url
        :param status: The reported status of the download
        :param message: A message describing the reason for setting the status
        :param exit_codes: A shared dict for all reports used by download_files
        """
        if exit_codes is not None:
            with self.__exit_code_lock:
                exit_codes[status][url] = message

    def download_file(
        self,
        url: str,
        output_dir: str,
        display_progress_bar: bool = False,
        output_buffer_list: Optional[list] = None,
        exit_codes: Optional[dict] = None,
    ) -> None:
        """
        Download a single DRS resource and output to a file or list

        :param url: The DRS resource url to download
        :param output_dir: The directory to download output to.
        :param display_progress_bar: Display a progress bar for the downloads to standard output
        :param output_buffer_list: If specified, output downloaded data to the list specified in the argument
        :param exit_codes: A shared dictionary of the exit statuses and messages
        :return:
        """
        try:
            drs_object = DRSObject(url)
        except ValueError as v:
            self.exit_download(
                url,
                DownloadStatus.FAIL,
                f"There was an error while parsing the DRS url ({v})",
                exit_codes,
            )
            return

        object_info_response = self.client.get(urljoin(drs_object.drs_server_url, f'objects/{drs_object.object_id}'))

        object_info_status_code = object_info_response.status_code
        if object_info_status_code != 200:
            if object_info_status_code == 404:
                error_msg = f"DRS object at url [{url}] does not exist"
            elif object_info_status_code == 403:
                error_msg = "Access Denied"
            else:
                error_msg = "There was an error getting object info from the DRS Client"
            self.exit_download(url, DownloadStatus.FAIL, error_msg, exit_codes)
            return

        object_info = object_info_response.json()
        download_url: Optional[str] = None

        if "access_methods" in object_info and object_info['access_methods']:
            for access_method in object_info["access_methods"]:
                if access_method["type"] != "https":
                    continue
                # try to use the access_id to get the download url
                if "access_id" in access_method.keys():
                    object_access_response = self.client.get(urljoin(drs_object.drs_server_url, f'objects/{drs_object.object_id}/access/{access_method["access_id"]}'))
                    object_access = object_access_response.json()
                    download_url = object_access["url"][0]
                    break
                # if we have a direct access_url for the access_method, use that
                elif "access_url" in access_method.keys():
                    download_url = access_method["access_url"]["url"]
                    break

            if not download_url:
                # we couldn't find a download url, exit unsuccessful
                self.exit_download(
                    url,
                    DownloadStatus.FAIL,
                    f"Error determining access method",
                    exit_codes,
                )
        else:
            return  # next page token, just return

        http_connection_pool = urllib3.PoolManager()
        chunk_size = 1024

        try:
            download_stream = http_connection_pool.request("GET", download_url, preload_content=False)
        except Exception as e:
            http_connection_pool.clear()
            self.exit_download(
                url,
                DownloadStatus.FAIL,
                f"There was an error downloading [{download_url}] : {e}",
                exit_codes,
            )
            return

        download_filename = get_filename_from_url(download_url)

        if output_buffer_list is not None:
            data = handle_file_response(download_filename, download_stream.read())
            with self.__output_lock:
                output_buffer_list.append(file_to_dataframe(download_filename, data))
        else:
            with open(f"{output_dir}/{download_filename}", "wb+") as dest:
                stream_size = int(download_stream.headers["Content-Length"])
                file_stream = download_stream.stream(chunk_size)
                if display_progress_bar:
                    click.echo(f"Downloading {url} into {output_dir}/{download_filename}...")
                    with click.progressbar(length=stream_size, color=True) as download_progress:
                        for chunk in file_stream:
                            dest.write(chunk)
                            download_progress.update(len(chunk))
                else:
                    for chunk in file_stream:
                        dest.write(chunk)
        http_connection_pool.clear()
        self.exit_download(
            url, DownloadStatus.SUCCESS, "Download Successful", exit_codes
        )

    def download_files(
        self,
        urls: List[str],
        output_dir: str = os.getcwd(),
        display_progress_bar: bool = False,
        out: List = None,
    ) -> None:
        """
        Download a list of files and output either to files in the current directory or dump to a specified list

        :param urls: A list of DRS resource urls to download
        :param output_dir: The directory to download output to.
        :param display_progress_bar: Display a progress bar for the downloads to standard output
        :param out: If specified, output downloaded data to the list specified in the argument
        :raises: DRSDownloadException if one or more of the downloads fail
        """
        download_threads = []
        exit_codes = {status: {} for status in DownloadStatus}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for url in urls:
            download = threading.Thread(
                target=self.download_file(
                    url,
                    output_dir,
                    display_progress_bar=display_progress_bar,
                    output_buffer_list=out,
                    exit_codes=exit_codes,
                ),
                name=url,
            )
            download.daemon = True
            download_threads.append(download)
            download.start()

        for thread in download_threads:
            thread.join()

        # at least one download failed, create exceptions
        failed_downloads = [
            DRSException(msg=msg, url=url)
            for url, msg in exit_codes.get(DownloadStatus.FAIL).items()
        ]
        if len(failed_downloads) > 0:
            raise DRSDownloadException(failed_downloads)
