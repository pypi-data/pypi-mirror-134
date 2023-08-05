"""Summary."""
import importlib.util
import inspect
import os
import re
import sys
from collections import OrderedDict
from importlib.abc import Loader
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import Callable, Generator, Match, Optional

from ergo.config import Config
from ergo.types import TYPE_PAYLOAD, TYPE_RETURN
from ergo.util import print_exc_plus


class FunctionInvocable:
    """Summary."""

    def __init__(self, config: Config) -> None:
        """Summary.

        Args:
            reference (str): Description

        """
        self._func: Optional[Callable[..., TYPE_RETURN]] = None  # type: ignore
        self._config: Config = config
        self.inject()

    @property
    def config(self) -> Config:
        """Summary.

        Returns:
            Config: Description

        """
        return self._config

    @property
    def func(self) -> Optional[Callable[..., TYPE_RETURN]]:  # type: ignore
        """Summary.

        Returns:
            Optional[Callable[..., TYPE_RETURN]]: Description

        """
        return self._func

    @func.setter
    def func(self, arg: Callable[..., TYPE_RETURN]) -> None:  # type: ignore
        """Summary.

        Args:
            arg (Callable[..., TYPE_RETURN]): Description

        """
        self._func = arg

    def invoke(self, data_in: TYPE_PAYLOAD) -> Generator[TYPE_PAYLOAD, TYPE_PAYLOAD, None]:
        """Invoke injected function.

        If func is a generator, will exhaust generator, yielding each response.
        If an exception occurs will re-raise with a stack trace.
        Func responses will not be percolated if they return None.

        Args:
            data_in (Dict): Contents will be passed to injected function as keyword args.

        Raises:
            Exception: caught exception re-raised with a stack trace.

        """
        if not self._func:
            raise Exception('Cannot execute injected function')
        try:
            args = [data_in.get(self.config.args[arg]) for arg in self.config.args]
            result = self._func(*args)
            if inspect.isgenerator(result):
                yield from result
            else:
                yield result
        except BaseException as err:
            raise Exception(print_exc_plus()) from err

    def inject(self) -> None:
        """Summary.

        Raises:
            Exception: Description

        """
        # [path/to/file/]<file>.<extension>[:[class.]method]]
        pattern: str = r'^(.*\/)?([^\.\/]+)\.([^\.]+):([^:]+\.)?([^:\.]+)$'  # (path/to/file/)(file).(extension):(method)
        matches: Optional[Match[str]] = re.match(pattern, self._config.func)
        if not matches:
            raise Exception(f'Unable to inject invalid referenced function {self._config.func}')

        path_to_source_file: str = matches.group(1)
        if not matches.group(1):
            path_to_source_file = os.getcwd()
        elif matches.group(1)[0] != '/':
            path_to_source_file = f'{os.getcwd()}/{matches.group(1)}'
        source_file_name: str = matches.group(2)
        source_file_extension: str = matches.group(3)
        sys.path.insert(0, path_to_source_file)

        spec: ModuleSpec = importlib.util.spec_from_file_location(source_file_name, f'{path_to_source_file}/{source_file_name}.{source_file_extension}')
        module: ModuleType = importlib.util.module_from_spec(spec)
        assert isinstance(spec.loader, Loader)  # see https://github.com/python/typeshed/issues/2793
        spec.loader.exec_module(module)

        scope: ModuleType = module
        if matches.group(4):
            class_name: str = matches.group(4)[:-1]
            scope = getattr(scope, class_name)

        method_name: str = matches.group(5)
        self._func = getattr(scope, method_name)
        self._config.args = OrderedDict((signature_arg, self._config.args.get(signature_arg, signature_arg)) for signature_arg in inspect.getfullargspec(self._func)[0])
