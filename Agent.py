
from States import GoHomeAndSleepUntilRested

"""
    The Agent class
"""
class Agent:
    # Constructor with default State
    def __init__(self):
        self.initial_state = GoHomeAndSleepUntilRested(self)
