
"""FLONICA PHIRI BSC-COM-28-19 Assignment 1 
Creating a class that houses all that the agent needs  inorder to operate
"""
#defining the class

class StateMachine:
    #defining the class Constructor with Agent And State

    def __init__(self, agent, state):
        self.agent = agent
        self.state = state

    # Instruct Agent to Start Working by using the initial state given to it
     
    def execute(self):
        self.agent.initial_state.execute()

    #  getting the Avalibale State in the Machine for the agent
    def get_available_transitions(self):
        return self.agent.initial_state.available_transitions()
