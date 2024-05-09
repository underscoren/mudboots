import importlib.util

if importlib.util.find_spec("pywinauto") is None:
    raise Exception("Please install pywinauto")