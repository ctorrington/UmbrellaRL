"""Grid World Environment."""


# TODO
    # (This is the Environment itself (nested dict with nested dict))
    # Loop through Grid Worlds State Space.
    
        # (This is the StateActions dict)
        # For every State, apply its available Actions.
        # Loop through each of those available Actions (StateActions)

            # (This is the StateProbabilityDistribution dict)
            # For every available Action (StateAction), apply the possible next States from that Action.
            # Loop through each possible next State & apply its probability of occuring.