import re

from .exception_executor import ExceptionExecutor
from ..modules_manager import ModulesManager


class ModuleSuggestExecutor(ExceptionExecutor):
    def execute(self, exception_type, value, tb):
        missing_name = re.findall(r"(?<=\')\w+(?=\')", str(value))[0]
        print(f"Module name '{missing_name}' is not declared, now searching the available modules.")

        # print(*traceback.format_tb(tb))
        # print(traceback.format_tb(tb)[-1].strip().split('\n')[-1].strip())

        if lines := self.modules_mgr.search(f"{missing_name}%"):
            for i, line in enumerate(lines):
                print(i + 1, line[4])
            # while lineno := input("Please select one to import :"):
            #     try:
            #         import_statement = str(lines[int(lineno) - 1][4])
            #         exception_code = str(traceback.format_tb(tb)[-1].strip().split('\n')[-1].strip())
            #         traceback.clear_frames(tb)
            #         exec(f"global os")
            #         exec(import_statement.strip())
            #         exec(exception_code.strip())
            #         break
            #     except:
            #         pass
        else:
            print("No match package found.")

    def __init__(self, name, print_trace=False):
        super(ExceptionExecutor, self).__init__()
        self.name = name
        self.print_trace = print_trace
        self.exception_type = NameError
        self.method = self.execute

        self.modules_mgr = ModulesManager()
        self.modules_mgr.init_db()
