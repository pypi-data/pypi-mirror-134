# -*- coding:utf-8 -*-
from typing import Dict, List

from fameio.source.scenario.agent import Agent
from fameio.source.scenario.contract import Contract
from fameio.source.scenario.exception import get_or_raise, log_and_raise
from fameio.source.scenario.fameiofactory import FameIOFactory
from fameio.source.scenario.generalproperties import GeneralProperties
from fameio.source.schema.schema import Schema
from fameio.source.tools import keys_to_lower


class Scenario:
    """Definition of a scenario"""

    _KEY_SCHEMA = "Schema".lower()
    _KEY_GENERAL = "GeneralProperties".lower()
    _KEY_AGENTS = "Agents".lower()
    _KEY_CONTRACTS = "Contracts".lower()

    _MISSING_KEY = "Scenario definition misses required key '{}'."
    _AGENT_ID_NOT_UNIQUE = "Agents ID not unique: '{}.'"
    _AGENT_TYPE_UNKNOWN = "Agent type '{}' not known in Schema."

    def __init__(self, schema: Schema, general_props: GeneralProperties) -> None:
        self._schema = schema
        self._general_props = general_props
        self._agents = list()
        self._agent_type_by_id = dict()
        self._contracts = list()

    @classmethod
    def from_dict(cls, definitions: dict, factory=FameIOFactory()) -> "Scenario":
        """Parse scenario from provided `definitions`"""
        definitions = keys_to_lower(definitions)

        schema = Schema.from_dict(
            get_or_raise(definitions, Scenario._KEY_SCHEMA, Scenario._MISSING_KEY)
        )
        general_props = GeneralProperties.from_dict(
            get_or_raise(definitions, Scenario._KEY_GENERAL, Scenario._MISSING_KEY)
        )
        result = cls(schema, general_props)

        for agent_definition in get_or_raise(
            definitions, Scenario._KEY_AGENTS, Scenario._MISSING_KEY
        ):
            result.add_agent(factory.new_agent_from_dict(agent_definition))

        for multi_definition in get_or_raise(
            definitions, Scenario._KEY_CONTRACTS, Scenario._MISSING_KEY
        ):
            for single_contract_definition in Contract.split_contract_definitions(
                multi_definition
            ):
                result.add_contract(
                    factory.new_contract_from_dict(single_contract_definition)
                )

        return result

    @property
    def agents(self) -> List[Agent]:
        """Returns all the agents of this scenario as a list"""
        return self._agents

    @property
    def agent_types_by_id(self) -> Dict[int, str]:
        """Returns dictionary of AgentTypes by agent-ids"""
        return self._agent_type_by_id

    def add_agent(self, agent: Agent) -> None:
        """Adds a new agent to this scenario

        Raises an Exception if the given agent id is not unique or its type name is unknown"""
        if agent.id in self._agent_type_by_id:
            log_and_raise(Scenario._AGENT_ID_NOT_UNIQUE.format(agent.id))
        if agent.type_name not in self._schema.agent_types:
            log_and_raise(Scenario._AGENT_TYPE_UNKNOWN.format(agent.type_name))
        self._agent_type_by_id[agent.id] = agent.type_name
        self._agents.append(agent)

    @property
    def contracts(self) -> List[Contract]:
        """Returns all the contracts of this scenario as a list"""
        return self._contracts

    def add_contract(self, contract: Contract) -> None:
        """Adds a new contract to this scenario"""
        self._contracts.append(contract)

    @property
    def schema(self) -> Schema:
        """Returns Schema associated with this scenario"""
        return self._schema

    @property
    def general_properties(self) -> GeneralProperties:
        """Returns General properties of this scenario"""
        return self._general_props
