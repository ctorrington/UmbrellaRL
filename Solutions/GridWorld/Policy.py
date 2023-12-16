"""
Grid World Policy.
"""

from src.StateIndex import StateIndex
from src.Action import Action
from src.StateSpace import StateSpace
from src.Policy.EquiprobablePolicy import EquiprobablePolicy

class GridWorldEquiprobablePolicy[SI: StateIndex, A: Action](EquiprobablePolicy[SI, A]):
    """Equiprobable Policy for Grid World."""
    
    def __init__(self,
                 state_space: StateSpace[SI, A]
                ) -> None:
        
        super().__init__(state_space)
