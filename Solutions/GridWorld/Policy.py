"""
Grid World Policy.
"""

from StateIndex import StateIndex # type: ignore
from Action import Action
from StateSpace import StateSpace

from Policy.EquiprobablePolicy import EquiprobablePolicy

class GridWorldEquiprobablePolicy[StateIndex, A: Action](EquiprobablePolicy[StateIndex, A]):
    """Equiprobable Policy for Grid World."""
    
    def __init__(self,
                 state_space: StateSpace[StateIndex, A]
                ) -> None:
        
        super().__init__(state_space)
