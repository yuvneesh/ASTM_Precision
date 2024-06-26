from __future__ import annotations
import os
import importlib
import pkgutil
from typing import Union, List, Dict
from .abstractASTM import AbstractASTM


def import_all():
    current_dir = os.path.dirname(__file__)
    for loader, module_name, is_pkg in pkgutil.walk_packages([current_dir]):
        if module_name.startswith('ASTM'):
            importlib.import_module('.' + module_name, 'ASTM_Precision')


def get_astm_method(test_method: str):
    """
    Return the appropriate ASTM method for the given test_method combination.
    """
    import_all()
    astm_method = AbstractASTM.registry[test_method]
    return astm_method


def is_list_of_numbers(var):
    return isinstance(var, list) and (all(isinstance(item, int) or isinstance(item, float) for item in var))


def validate_dict(data):
    expected_keys = {'test_method', 'data'}
    if not all(key in data for key in expected_keys):
        return False
    if not isinstance(data['test_method'], str):
        return False
    if not is_list_of_numbers(data['data']):
        return False
    return True


def analyze(data: Dict[str, Union[List[int, float], str]]):
    # if not validate_dict(data):
    #    raise InvalidFormat

    astm_method = get_astm_method(data['test_method'])
    instantiated = astm_method(data['data'])
    return instantiated.validate_data()


def available_methods():
    import_all()
    methods = []
    for k, v in AbstractASTM.registry.items():
        identifiable_name = k
        display_name = " ".join(str(v).split(".")[1].split("_")[2:])
        methods.append((identifiable_name, display_name))
    return methods


class InvalidFormat(Exception):
    def __init__(self, message="Invalid format"):
        self.message = message
        super().__init__(self.message)

