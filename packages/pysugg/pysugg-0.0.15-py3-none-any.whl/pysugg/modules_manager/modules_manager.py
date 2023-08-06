import os
import re
import site
import sqlite3
import sys
import uuid
from contextlib import closing
from sqlite3 import Cursor


class ModulesManager:
    def __init__(self, search_paths: list = None):
        self.uuid = uuid.uuid4().hex
        self.con = sqlite3.connect(":memory:")
        self.table_name = f'module_manager_{self.uuid}'
        self.search_paths = {*sys.path, *site.getsitepackages()} if search_paths is None else search_paths

    def init_db(self):
        self.drop_and_create_table()
        self.collect_modules()

    def drop_and_create_table(self):
        # print(f"drop_and_create_table, {self.table_name}")

        with closing(self.con.cursor()) as csr:
            csr.execute(f"DROP TABLE IF EXISTS {self.table_name};")
            csr.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.table_name}
                    (id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    module_type TEXT    NOT NULL,
                    package     TEXT    NOT NULL,
                    module      TEXT    NOT NULL,
                    statement   TEXT    NOT NULL,
                    use_count   INTEGER DEFAULT 0);                  
                    ''')

    def insert_into(self, cursor: Cursor, module_type, package, module, statement, use_count=0):
        cursor.execute(f'''INSERT INTO {self.table_name}
                            VALUES(null,'{module_type}','{package}','{module}','{statement}','{use_count}')''')

    def collect_modules(self):
        function_re = re.compile(r"(?<=^def)\s+\w*")
        class_re = re.compile(r"(?<=^class)\s+\w*")
        variable_re = re.compile(r"^\w+(?=\s=)")

        rexps = [type("TempRe", (), {'module_type': 'function', 're': function_re}),
                 type("TempRe", (), {'module_type': 'class', 're': class_re}),
                 type("TempRe", (), {'module_type': 'variable', 're': variable_re})]

        with closing(self.con.cursor()) as csr:
            for search_path in self.search_paths:
                for root, dirs, files in os.walk(search_path):
                    # 暂时不考虑文件夹
                    # for dire in dirs:
                    #     print(os.path.join(root, dire))
                    for file in filter(lambda x: str(x).endswith('.py'), files):
                        # print(package_path)
                        # print(os.path.join(root, file))
                        package = os.path.join(root, file) \
                            .replace(f'{search_path}/', '') \
                            .replace('.py', '') \
                            .replace('/', '.')

                        self.insert_into(csr, 'module', package, package, f'import {package}')

                        with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                            for line in f.readlines():
                                for rexp in rexps:  # 使用三种re分别作用于行
                                    if (mod := rexp.re.findall(line)) and (mod := str(mod[0]).strip()):
                                        self.insert_into(csr, rexp.module_type, package, mod,
                                                         f'from {package} import {mod}')
                                        break

    def search(self, module_name_exp: str, *, limit=5):
        """
        :param module_name_exp:
        :param limit:
        :return: (7673, 'class', 'site-packages.flask.app', 'Flask', 'from site-packages.flask.app import Flask', 0)
        """
        with closing(self.con.cursor()) as csr:
            csr.execute(f'''SELECT * FROM {self.table_name} 
                             WHERE lower({self.table_name}.MODULE) LIKE '{module_name_exp}'
                             ORDER BY LENGTH(module) * 5 + LENGTH(package)
                             LIMIT {limit}''')
            return csr.fetchall()
