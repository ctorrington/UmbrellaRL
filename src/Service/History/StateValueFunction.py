"""State Value Function class for storing the recorded State Value Function."""

from typing import Any, Dict

from numpy import float64
import numpy.typing as npt

class StateValueFunction(Dict[str, npt.NDArray[float64]]):
    """
    State Value Function class for storing the recorded State Value Function.
    """
    
    def __init__(self,
        state_value_function: Dict[str, npt.NDArray[float64]]
    ) -> None:
        
        super().__init__(state_value_function)
        
    def __getattribute__(self, __name: str) -> npt.NDArray[float64]:
        return super().__getattribute__(__name)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)