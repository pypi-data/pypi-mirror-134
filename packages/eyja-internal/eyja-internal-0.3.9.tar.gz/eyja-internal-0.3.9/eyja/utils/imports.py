import importlib
import inspect


def load_class(class_path):
    parts = class_path.split('.')
    module_path = '.'.join(parts[:-1])
    module = importlib.import_module(module_path)
    cls = getattr(module, parts[-1])
    if inspect.isclass(cls):
        return cls
    
    return None
