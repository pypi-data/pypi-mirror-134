# DNAstack Client Library
`dnastack` is the command line interface and Python library for DNAstack products. This project is written in Python and uses the [Click](https://click.palletsprojects.com/en/7.x/) CLI framework.

### Table of Contents
- [Getting Started](#getting-started)
- [Distributing the CLI](#distributing-the-clipython-library)
- [API Reference](#api-references)
- [Authorization](#authorization)
- [Testing](#testing)

## Getting Started

### Prerequisites

* Mandatory
  * Any versions of Python 3 which are currently officially supported (bugfix or security).
* Optional
  * `pandas` for anything functionalities which require `pandas.DataFrame`.

### Installation

#### Install the package with `pip`

> **Warning:** This approach will share dependencies with what you have in your environment (global or virtual).
> If you need to install the package just to use the command line in isolation, i.e., without changing your environment,
> please [install with `pipx`](#install-the-package-with-pipx) instead.

You just need to run:

```shell
pip3 install dnastack-client-library>=2.0
```

Unlike **version 1**, this is designed to be platform-agnostic.

#### Install the package with `pipx`

> **Warning:** The approach will only install the package as a command line tool. You will not be able to use the
> installed package in your Python code or Jupyter notebook.

1. Ensure that you have [pipx](https://pypa.github.io/pipx/).
2. Run `pipx install dnastack-client-library`.

#### Install the package from the source code

> **Warning:** The version of the package in the source code is fixed and may be behind the published version. Please uninstall the installed one with `pip3 uninstall` before proceeding.

Once you have a copy of the source code, from the root you may just run:

```shell
pip3 install -IU .
```

### Usage

#### Command line
```shell
dnastack config set data_connect.url https://collection-service.publisher.dnastack.com/collection/library/search/
dnastack dataconnect tables list
dnastack dataconnect tables get covid.cloud.variants
dnastack dataconnect query "SELECT drs_url FROM covid.cloud.files LIMIT 10"
```

Alternatively, you can also do this.

```shell
python3 -m dnastack config set data_connect.url https://collection-service.publisher.dnastack.com/collection/library/search/
python3 -m dnastack dataconnect tables list
python3 -m dnastack dataconnect tables get covid.cloud.variants
python3 -m dnastack dataconnect query "SELECT drs_url FROM covid.cloud.files LIMIT 10"
```

> **Tip:** The latter also works when you run `python3 -m dnastack` from the root of this project when the package is not installed.

#### Library

Simply import the `PublisherClient` object

`from dnastack import PublisherClient`

#### Example

```python
from dnastack import PublisherClient

publisher_client = PublisherClient(dataconnect_url='[DATACONNECT_URL]')
# get tables
tables = publisher_client.dataconnect.list_tables()
# get table schema
schema = publisher_client.dataconnect.get_table('[TABLE_NAME]')
# query a table
results = publisher_client.dataconnect.query('SELECT * FROM ...')
```

If your environment has `pandas`, you can also do this.

```python
import pandas as pd

# load a drs resource into a DataFrame
drs_df = pd.DataFrame(publisher_client.load(['[DRS_URL]']))
# download a DRS resource into a file
publisher_client.download(['[DRS_URL]'])
```

## Distributing the CLI/Python library

### Versioning

This is based on `git describe`. While the development version will be fixed to a certain version, the published version
will be determined during the build by `scripts/build-package.py`

### Building the package

From your terminal app of choices, run `scripts/build-package.py`. The built package will be in `dist/`.

### CI/CD Pipeline

In it's current state, the CI/CD pipeline for the dnastack-client-library:

1. Builds the *Linux* excutable of the CLI (Windows and Mac executables need to be built manually)
2. Publishes the available executables (i.e. the ones in the `dist` folder) to Github Releases
3. Builds and publishes the PyPI package.

These processes are all triggered after every push to the `main` branch of the repo.
You should not need to do any of the above manually.

The [cloudbuild.yaml](./cloudbuild.yaml) file in the root directory specifies the steps to be run by Google Cloud Build

The CI/CD pipeline also makes use of a bootstrap workspace to store secrets used in distribution.
More information of how this workspace is used and how to add/modify secrets can be found [here](docs/bootstrap-workspace.md)

## API References

**Note:** These references are not complete and very much a work in progress.

CLI: [CLI Reference](docs/reference/cli.md)


## Authorization

In the CLI, we use Wallet clients in order to authorize users to access Data Connect, Collections, DRS, and WES functionality.

### Passport
In order to log in to get an access token:

1. Make sure the client is correctly configured. You need to log in with the Wallet instance
   associated with the service you are trying to gain access for. Information on creating a client and exisitng
   configurations can be found [here](docs/clients.md). In order to set this configuration, run:
```bash
dnastack config set [SERVICE].auth.url [WALLET-URL]
dnastack config set [SERVICE].auth.client.id [CLIENT-ID]
dnastack config set [SERVICE].auth.client.secret [CLIENT-SECRET]
dnastack config set [SERVICE].auth.client.redirect_url [REDIRECT-URI]
```
2. Log in using `dnastack auth login [SERVICE]`. This will open a tab in your browser where you may login, then allow/deny access
   to certain permissions. If allowed, a new token will be created and you will be able to access services.

### Refresh Token

Since the above requires user interaction to authenticate, it cannot be used in headless environments such as scripts.
The way that users should log in is through an OAuth refresh token.

In order to get an access token in a headless environment:

1. Manually generate a refresh token using the following script. This will require you to sign in using Passport.
   The result of the final command will be a refresh_token for the service
```bash
# configure your service's oauth client
dnastack config set [SERVICE].auth.url [BASE AUTH URL]
dnastack config set [SERVICE].auth.client.id [CLIENT ID]
dnastack config set [SERVICE].auth.client.secret [CLIENT SECRET]
dnastack config set [SERVICE].auth.client.redirect_url [CLIENT SECRET]

# configure the service url
dnastack config set [SERVICE].url [SERVICE URL]

# log in with that service
dnastack auth login [SERVICE]

# get the token
dnastack config get [SERVICE].auth.refresh_token
```

2. In the headless environment, when log in is required, run
```bash
# configure your service's oauth client to the same as log in
dnastack config set [SERVICE].auth.url [BASE AUTH URL]
dnastack config set [SERVICE].auth.client.id [CLIENT ID]
dnastack config set [SERVICE].auth.client.secret [CLIENT SECRET]
dnastack config set [SERVICE].auth.client.redirect_url [CLIENT SECRET]

dnastack config set [SERVICE].auth.refresh_token [TOKEN]
```


## Testing

There are e2e-tests set up for the CLI. Instructions to run can be found [here](docs/e2e-tests.md)
