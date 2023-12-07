"""
Grid World Policy.
"""

from src.StateIndex import StateIndex # type: ignore
from src.Action import Action
from src.StateSpace import StateSpace

from src.Policy.EquiprobablePolicy import EquiprobablePolicy

class GridWorldEquiprobablePolicy[StateIndex, A: Action](EquiprobablePolicy[StateIndex, A]):
    """Equiprobable Policy for Grid World."""
    
    def __init__(self,
                 state_space: StateSpace[StateIndex, A]
                ) -> None:
        
        super().__init__(state_space)
