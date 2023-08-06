class ExceptionExecutor:
    def __init__(self, name, exception_type, method, print_trace=False):
        self.name = name
        self.exception_type = exception_type
        self.method = method
        self.print_trace = print_trace
