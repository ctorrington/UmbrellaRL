"""State Space for the Grid World."""

from typing import Dict, List, Tuple

from StateSpace import StateSpace

index_type = Tuple[int, int]

class GridWorldStateSpace(StateSpace[index_type]):
    """Grid World State Space representation."""