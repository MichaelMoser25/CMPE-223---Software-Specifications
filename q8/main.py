""" 
Probelm 8:
Write a program (in C, C++, Java, or Python) that takes a finite automaton 
description (in the 5-tuple format) and a string as input, and determines 
whether the automaton accepts the string.

    fa_description = {
        "states": {"q0", "q1", "q2"},
        "alphabet": {"0", "1"},
        "transitions": {
            ("q0", "0"): "q1",
            ("q0", "1"): "q0",
            ("q1", "0"): "q2",
            ("q1", "1"): "q0",
            ("q2", "0"): "q2",
            ("q2", "1"): "q2",
        },
        "start_state": "q0",
        "accept_state": {"q2"},
    }

    input_strings = ["0" , "01" , "001" , "0001" , "111" , "10" , "000"]
"""

class FiniteAutomation:
   # Initialize FA with 5-tuple description 
   def __init__(self, description):
       self.states = description["states"]           # Set of states
       self.alphabet = description["alphabet"]       # Input alphabet
       self.transitions = description["transitions"] # Transition function
       self.start_state = description["start_state"] # Initial state
       self.accept_states = description["accept_state"] # Set of accept states

   # Process input string and determine if accepted
   def proc_string(self, input_string):
       current_state = self.start_state  # Start from initial state
       
       # Process each character in input string
       for char in input_string:
           # Reject if character not in alphabet
           if char not in self.alphabet:
               return False
           # Reject if no valid transition exists
           elif (current_state, char) not in self.transitions:
               return False
           # Update current state based on transition
           current_state = self.transitions[(current_state, char)]
           
       # Accept if final state is an accept state
       return current_state in self.accept_states

def main():
   # Define the FA using 5-tuple format
   fa_description = {
       "states": {"q0", "q1", "q2"},
       "alphabet": {"0", "1"}, 
       "transitions": {
           ("q0", "0"): "q1",
           ("q0", "1"): "q0",
           ("q1", "0"): "q2", 
           ("q1", "1"): "q0",
           ("q2", "0"): "q2",
           ("q2", "1"): "q2",
       },
       "start_state": "q0",
       "accept_state": {"q2"},
   }

   # Create FA instance and test input strings
   fa = FiniteAutomation(fa_description)
   input_strings = ["0", "01", "001", "0001", "111", "10", "000"]
   
   # Process each string and print result
   for string in input_strings:
       accepted = fa.proc_string(string)
       print(f"Input: {string} --> Accepted: {accepted}")

# Run main function when script is executed
if __name__ == "__main__":
   main()
