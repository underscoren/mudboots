import importlib.util

if importlib.util.find_spec("xdo") is None:
    raise Exception("Please install python-libxdo")