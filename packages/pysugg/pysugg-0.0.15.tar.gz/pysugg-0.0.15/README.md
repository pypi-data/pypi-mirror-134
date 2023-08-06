This package is designed to give some troubles when exceptions occurred.

Like the sample below, it gives you an import suggest, in the situation that the package flask is not imported.

python code:

```python
from src.pysugg.exception_catcher import ExceptionCatcher
from src.pysugg.exception_executors.module_suggest_executor import ModuleSuggestExecutor

ExceptionCatcher().add_executor(ModuleSuggestExecutor("test", print_trace=True)).start()

# For test, you can see we have not imported the 'os' module, but no error raise as usual here.
# And, you will find suggested import statements.
flask
```

output:
```
Module name 'flask' is not declared, now searching the available modules.
Traceback (most recent call last):
  File "/Users/bitekong/PycharmProjects/pysugg/test.py", line 8, in <module>
    flask
NameError: name 'flask' is not defined
1 from flask.app import Flask
2 from site-packages.flask.app import Flask
3 import flask.cli
4 import flask.app
5 import flask.ctx
```

In the time that the module name is very long or the hierarchy of the module is very deep, 
it's very useful in Jupiter which is without the `auto-import feature`, a feature initially occurring in Pycharm.

These modules support you can easy to choose which module should be imported.

In the soon next version, `pysugg` is considered to support the `pip auto download` feature,
which can save you much time to search the package you did not import and download.

