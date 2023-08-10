"""
Constants.
"""

class Constants:

    class ACTIONS:
        LEFT = "LEFT"
        RIGHT = "RIGHT"

        @staticmethod
        def as_tuple():
            return Constants.ACTIONS.LEFT, Constants.ACTIONS.RIGHT