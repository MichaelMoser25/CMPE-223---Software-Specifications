# Problem 8
- This code implements a Finite Automation (FA) that processes binary strings (0s and 1s) 
- The FA has three states (q0, q1, q2) and accepts strings based on defined transitions 
- The class can be used for any FA by providing a different description dictionary 

How to Run: 
- Save the code as finite_automation.py 
- Run using Python 3.x: python finite_automation.py 
- The program will test several input strings and show if they're accepted 
 
- FiniteAutomation class: 
  - Takes a description dictionary defining the FA 
  - proc_string method processes input strings and determines if they're accepted 
- The example FA in main(): 
  - Has states q0, q1, q2 
  - Accepts strings that contain "00" (will end in state q2) 
  - Will show which test strings are accepted/rejected 
