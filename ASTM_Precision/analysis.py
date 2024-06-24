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


def get_astm_method(method_number: str, analyte_name: str):
    """
    Return the appropriate ASTM method for the given method/analyte combination.
    """
    import_all()
    search_key = "ASTM" + method_number + analyte_name
    search_key = search_key.replace(" ", "")
    astm_method = AbstractASTM.registry[search_key]
    return astm_method


def is_list_of_numbers(var):
    return isinstance(var, list) and (all(isinstance(item, int) or isinstance(item, float) for item in var))


def validate_dict(data):
    expected_keys = {'method', 'analyte', 'data'}
    if not all(key in data for key in expected_keys):
        return False
    if not isinstance(data['method'], str):
        return False
    if not isinstance(data['analyte'], str):
        return False
    if not is_list_of_numbers(data['data']):
        return False
    return True


def analyze(data: Dict[str, Union[List[int, float], str]]):
    if not validate_dict(data):
        raise InvalidFormat

    astm_method = get_astm_method(data['method'], data['analyte'])
    instantiated = astm_method(data['data'])
    return instantiated.validate_data()


class InvalidFormat(Exception):
    def __init__(self, message="Invalid format"):
        self.message = message
        super().__init__(self.message)

