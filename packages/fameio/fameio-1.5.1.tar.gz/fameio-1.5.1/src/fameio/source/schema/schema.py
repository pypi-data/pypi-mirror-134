# -*- coding:utf-8 -*-

from typing import Dict

from fameio.source.logs import log_error_and_raise
from fameio.source.schema.agenttype import AgentType
from fameio.source.schema.exception import SchemaException
from fameio.source.tools import keys_to_lower


class Schema:
    """Definition of a schema"""

    _AGENT_TYPES_MISSING = "Keyword AgentTypes not found in Schema."
    _KEY_AGENT_TYPE = "AgentTypes".lower()

    def __init__(self):
        self._agent_types = dict()

    @classmethod
    def from_dict(cls, definitions: dict) -> "Schema":
        """Load definitions from given `schema`"""
        definition = keys_to_lower(definitions)
        if Schema._KEY_AGENT_TYPE not in definition:
            log_error_and_raise(SchemaException(Schema._AGENT_TYPES_MISSING))

        result = cls()
        for agent_type_name, agent_definition in definition[
            Schema._KEY_AGENT_TYPE
        ].items():
            result.add_agent_type(
                AgentType.from_dict(agent_type_name, agent_definition)
            )

        return result

    @property
    def agent_types(self) -> Dict[str, AgentType]:
        """Returns all the agent types by their name"""
        return self._agent_types

    def add_agent_type(self, agent_type: AgentType):
        """Adds a new agent type to the Schema"""
        self._agent_types[agent_type.name] = agent_type
