# -*- coding:utf-8 -*-
import logging as log
from typing import Any, Dict, List

from fameio.source.scenario.exception import log_and_raise


class Attribute:
    """An Attribute of an agent in a scenario"""

    _VALUE_MISSING = "Value not specified for Attribute '{}' - leave out if default shall be used (if defined)."
    _OVERWRITE = (
        "Value already defined for Attribute '{}' - overwriting value with new one!"
    )
    _LIST_EMPTY = "Attribute '{}' was assigned an empty list - please remove or fill empty assignments."
    _DICT_EMPTY = "Attribute '{}' was assigned an empty dictionary - please remove or fill empty assignments."
    _MIXED_DATA = "Attribute '{}' was assigned a list with mixed complex and simple entries - please fix."

    def __init__(self, name: str, definitions) -> None:
        """Parses an Attribute's definition"""
        self._full_name = name

        if definitions is None:
            log_and_raise(Attribute._VALUE_MISSING.format(name))

        if isinstance(definitions, dict):
            self.value = None
            self.nested_list = None
            self.nested = Attribute._build_attribute_dict(name, definitions)
        elif Attribute._is_list_of_dict(name, definitions):
            self.nested = None
            self.value = None
            self.nested_list = list()
            for entry in definitions:
                self.nested_list.append(Attribute._build_attribute_dict(name, entry))
        else:
            self.nested = None
            self.nested_list = None
            self.value = definitions

    @staticmethod
    def _build_attribute_dict(
        name: str, definitions: Dict[str, Any]
    ) -> Dict[str, "Attribute"]:
        """Returns a new dictionary containing Attributes generated from given `definitions`"""
        if not definitions:
            log_and_raise(Attribute._DICT_EMPTY.format(name))

        dictionary = dict()
        for nested_name, value in definitions.items():
            full_name = name + "." + nested_name
            if nested_name in dictionary:
                log.warning(Attribute._OVERWRITE.format(full_name))
            dictionary[nested_name] = Attribute(full_name, value)
        return dictionary

    @staticmethod
    def _is_list_of_dict(name: str, definitions: Any) -> bool:
        """Returns True if given `definitions` is a list of dict"""
        if isinstance(definitions, list):
            if not definitions:
                log_and_raise(Attribute._LIST_EMPTY.format(name))

            all_dicts = no_dicts = True
            for item in definitions:
                if not isinstance(item, dict):
                    all_dicts = False
                else:
                    no_dicts = False
            if (not all_dicts) and (not no_dicts):
                log_and_raise(Attribute._MIXED_DATA.format(name))
            return all_dicts
        return False

    def has_nested(self) -> bool:
        """Returns True if nested Attributes are present"""
        return bool(self.nested)

    def has_nested_list(self) -> bool:
        """Returns True if list of nested items are present"""
        return bool(self.nested_list)

    def get_nested_by_name(self, key: str) -> "Attribute":
        """Returns nested Attribute by specified name"""
        return self.nested[key]

    def get_nested_list(self) -> List[Dict[str, "Attribute"]]:
        """Return list of all nested Attribute dictionaries"""
        return self.nested_list

    def get_nested(self) -> Dict[str, "Attribute"]:
        """Returns dictionary of all nested Attributes"""
        return self.nested

    def has_value(self) -> bool:
        """Returns True if Attribute has any value assigned"""
        return self.value is not None

    def __repr__(self) -> str:
        return self._full_name
