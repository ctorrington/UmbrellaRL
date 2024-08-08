"""
Grid World Policy.
"""

from core.dependency.state_index import StateIndex
from core.dependency.action import Action
from core.dependency.state_space import StateSpace
from core.Policy.EquiprobablePolicy import EquiprobablePolicy

from log.ilogger import ILogger

class GridWorldEquiprobablePolicy[SI: StateIndex, A: Action](EquiprobablePolicy[SI, A]):
    """Equiprobable Policy for Grid World."""
    
    def __init__(
        self,
        state_space: StateSpace[SI, A],
        logger: ILogger
    ) -> None:
        super().__init__(
            state_space,
            logger=logger
        )
