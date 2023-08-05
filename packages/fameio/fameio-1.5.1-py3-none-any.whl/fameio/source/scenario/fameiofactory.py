# -*- coding:utf-8 -*-
from fameio.source.scenario.agent import Agent
from fameio.source.scenario.contract import Contract


class FameIOFactory:
    """Factory used to instanciate the types defined in a scenario file.

    This allows a client to subclass some types in order to extend what a scenario can contain.
    """

    @staticmethod
    def new_agent_from_dict(definitions: dict) -> Agent:
        """Constructs a new Agent from provided `definitions`"""
        return Agent.from_dict(definitions)

    @staticmethod
    def new_contract_from_dict(definitions: dict) -> Contract:
        """Constructs a new Contract from provided `definitions`"""
        return Contract.from_dict(definitions)
