"""
History class for recording changes in the state value function & policy 
actions.
"""

from typing import Dict

from numpy import float64
import numpy.typing as npt

class History(Dict[int, Dict[npt.NDArray[float64] | List[A]]]):
    """
    History class for recording changes in the State Value Function & Policy 
    Actions.
    """
    
    def timestep(self,
        n: int
    ) -> npt.NDArray[float64]:
        """
        Get the State Value Function & Policy Actions at the given timetstep.
        """