
from StateMachine import StateMachine
"""
    Defining the State Base Class which is the super class of all the child states of the agent.
    
"""

class States:
    # Constructor
    def __init__(self, agent):
        self.agent = agent
# defining the execution self for the class by passing the states to the agent given the transitions
    def execute(self):
        pass

#  defining the Go and Sleep State Until Rested  Class
class GoHomeAndSleepUntilRested(States):
    # This stateof the gohome and sleep class and Super Constructors
    def __init__(self, agent):
        super().__init__(agent)

    # Ruturn the reachable state for the agent

    def available_transitions(self):
        return [ "GoToWorkplaceAndMakeMoney"]

    def execute(self):
        # An object of the  State Machine
        fsm = StateMachine(self.agent, self)

        # initial location of the agent
        print("\nThe Employee is at Home and sleeping until rested.")
        print(f"Employee reachable State :{fsm.get_available_transitions()}")
        options = [" \n1. Not Fatigued"," \n2. Quit"]

        # Display the current State the agent is
        print(f"Employee Current state: {type(self.agent.initial_state).__name__}\n\nSelect available transition state Options: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switching Agent from this Home to Work Place
            self.agent.initial_state = GoToWorkplaceAndMakeMoney(self.agent)
            
        elif choice == "2":
            print("An Agent is leaving!!!")
            # Leaving  the State
            exit(2)

            # Go To Bank And Deposite Money State Class
class GoToTheBankAndDepositMoney(States):
    # This Class Constructor
    def __init__(self, agent):
        # Super Class Constructor
        super().__init__(agent)

    # Reachable States
    def available_transitions(self):
        return ["GoToWorkplaceAndMakeMoney", "GoHomeAndSleepUntilRested"]

    def execute(self):
        fsm = StateMachine(self.agent, self)
        # The Location of the agent
        print("\nThe Employee is at the bank and depositing money.")
        # The States That Can be Transitioned
        print(f"Employee Reachable States are:{fsm.get_available_transitions()}")
        # The Transtions for the agent
        options = ["\n1. Not Satisfied With Amount In Bank","\n2. Satisfied With Amount In Bank","\n3. Quit"]

        # Display The Current State the agent is in
        print(f"Employee Current state: {type(self.agent.initial_state).__name__}\n\nSelect available transition state Options: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switch the Agent form This State to Work Place
            self.agent.initial_state = GoToWorkplaceAndMakeMoney(self.agent)
        elif choice == "2":
            # Switch the Agent form This State to Home to Rest
            self.agent.initial_state = GoHomeAndSleepUntilRested(self.agent)
        elif choice == "3":
            # Quiting Action
            print("An Agent is leaving!!!")
            exit(2)

# Go to Work Place And Male Money State Class
class GoToWorkplaceAndMakeMoney(States):
    # Constructor
    def __init__(self, agent):
        # Super Class Constructor
        super().__init__(agent)

    # Reachable States
    def available_transitions(self):
        return ["GoToTheBankAndDepositMoney", "SatisfyHungerAtRestaurant"]

    def execute(self):
        # Finite Machine for the Agent to Work on
        fsm = StateMachine(self.agent, self)
        # The Agent Present Location
        print("\nThe Employee is at the workplace and making money.")
        # Reachable States from this State
        print(f"Employee Reachable States :{fsm.get_available_transitions()}")
        # The Transition for the Agent 
        options = ["\n1. Has Made Enough Money","\n2. Is Hungry","\n3. Quit"]
        # The Present State 
        print(f"Employee Current state: {type(self.agent.initial_state).__name__}\n\nSelect available transition state Options: {'  '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
             # Switch the Agent form This State to The Bank and Deposite Money
            self.agent.initial_state = GoToTheBankAndDepositMoney(self.agent)
        elif choice == "2":
             # Switch the Agent form This State to Satisfy Hunger State 
            self.agent.initial_state = SatisfyHungerAtRestaurant(self.agent)
        elif choice == "3":
            # Quiting Action
            print("An Agent is leaving!!!")
            exit(2)
            

# Go to Returant And Satisfy Hunger State class
class SatisfyHungerAtRestaurant(States):
    # This class and Super class Constructors
    def __init__(self, agent):
        super().__init__(agent)

    # Reachable State
    def available_transitions(self):
        return ["GoToWorkplaceAndMakeMoney"]

    def execute(self):
        # Finite Machine for the Agent to Work on
        fsm = StateMachine(self.agent, self)
        print("\nThe Employee is at the restaurant satisfying hunger.")
        print(f"Employee Reachable State :{fsm.get_available_transitions()}")
        # The Transitons for the Agent
        options = ["\n1. Not Hungry","\n2. Quit"]
        # Pressent State 
        print(f"Employee Current state: {type(self.agent.initial_state).__name__}\n\nSelect available tansition state Options: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switch the Agent form This State to Work place And Make Money
            self.agent.initial_state = GoToWorkplaceAndMakeMoney(self.agent)

        elif choice == "2":
            # Quiting the Action
            print("An Agent is leaving!!!")
            exit(2)