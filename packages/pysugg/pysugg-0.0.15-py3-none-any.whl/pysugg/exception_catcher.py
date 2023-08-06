import sys
import traceback
from typing import Callable, Any
from .exception_executors.exception_executor import ExceptionExecutor


class ExceptionHandler(object):
    def __init__(self):
        self.exception_executors: dict[ExceptionExecutor] = dict()

    def add_executor(self, exception_executor: ExceptionExecutor):
        self.exception_executors[exception_executor.name] = exception_executor

    def remove_executor(self, name: str):
        del self.exception_executors[name]

    def __call__(self, *exception_info):

        """Handles exceptions"""
        exception_info = exception_info or sys.exc_info()
        exception_type, value, tb = exception_info
        # print(exception_type, value, tb)

        if available_executors := list(filter(lambda x: x[1].exception_type == exception_type,
                                              self.exception_executors.items())):
            for key, exception_executor in available_executors:  # type: str, ExceptionExecutor
                if exception_executor.print_trace:
                    sys.stderr.write("".join(traceback.format_exception(exception_type, value, tb)))
                    sys.stderr.flush()
                try:
                    exception_executor.method(exception_type, value, tb)
                except:
                    print(f"Exception executor '{exception_executor.name}' threw an Exception.")
                    sys.stderr.write(traceback.format_exc())
                    sys.stderr.flush()
        else:
            print(f"No match exception executor.")
            sys.__excepthook__(exception_type, value, tb)

    def as_ipython_handler(self):
        def handle_ipython(shell, exception_type, value, tb, tb_offset=None):
            # shell.showtraceback((exception_type, value, tb), tb_offset=tb_offset)
            self(exception_type, value, tb)
            return traceback.format_tb(tb)

        return handle_ipython


class ExceptionCatcher:
    def __init__(self):
        self.exception_handler = ExceptionHandler()

    def add_executor(self, exception_executor: ExceptionExecutor):
        self.exception_handler.add_executor(exception_executor=exception_executor)
        return self

    def add_executor_method(self, name, exception_type,
                            method: Callable[[Exception, str, Any], None], print_trace=False):
        exception_executor = ExceptionExecutor(name=name, exception_type=exception_type, method=method,
                                               print_trace=print_trace)
        self.exception_handler.add_executor(exception_executor=exception_executor)
        return self

    def start(self):
        try:
            # print("ipython_shell")
            ipython_shell = get_ipython()
            ipython_shell.set_custom_exc((Exception,), self.exception_handler.as_ipython_handler())
        except NameError as e:
            # print("base")
            sys.excepthook = self.exception_handler
        return self
