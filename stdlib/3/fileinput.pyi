from typing import Iterable, BinaryIO, List, Callable, IO


def input(
    files: List[str]=...,
    inplace: bool=...,
    backup: str=...,
    bufsize: int=...,
    mode: str=...,
    openhook: Callable[[str, str], IO[AnyStr]]=...
    ): ...


def close() -> None: ...
def nextfile() -> None: ...
def filename() -> str: ...
def lineno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...

class FileInput(Iterable):
    def __init__(
        self,
        files: List[str]=...,
        inplace: bool=...,
        backup: str=...,
        bufsize: int=...,
        mode: str=...,
        openhook: Callable[[str, str], IO[AnyStr]]=...
        ) -> None: ...

    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> str: ...
    def __getitem__(self, i) -> str: ...
    def nextfile(self) -> None: ...
    def readline(self) -> str: ...
    def filename(self) -> str: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...

def hook_compressed(filename: str, mode: str) -> IO[AnyStr]: ...
def hook_encoded(encoding: str) -> IO[AnyStr]: ...
