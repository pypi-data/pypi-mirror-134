from abc import ABC
from threading import Lock
from typing import Any, Dict, List


class ResultLoader(ABC):
    def load(self) -> List[Dict[str, Any]]:
        ...

    def has_more(self) -> bool:
        ...

    def close(self):
        ...


class ResultIterator:
    def __init__(self, loader: ResultLoader):
        self.__read_lock = Lock()
        self.__loader = loader
        self.__buffer: List[Dict[str, Any]] = []
        self.__depleted = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.__depleted:
            self.__loader.close()
            raise StopIteration('Already depleted')

        with self.__read_lock:
            while not self.__buffer:
                # Refill the buffer
                if not self.__buffer and not self.__depleted:
                    if self.__loader.has_more():
                        self.__buffer.extend(self.__loader.load())
                    else:
                        self.__depleted = True
                        raise StopIteration('No more result to iterate')

            # Read within the lock
            item = self.__buffer.pop(0)

        return item
