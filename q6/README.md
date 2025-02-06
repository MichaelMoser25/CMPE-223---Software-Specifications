# Problem 6
- This is an email validator that uses a state machine to check if an email address is valid 
- The validator checks for proper format: username@domain.tld (e.g., user@example.com) 
- The code includes both the validator class and unit tests to verify it works correctly 
- It checks for common email rules like: 
  - Valid characters in username (letters, numbers, ., _, -) 
  - Valid characters in domain (letters, numbers, -) 
  - Proper TLD length (must be 2+ characters) 
  - Proper placement of special characters 

How to Run: 

- Save the code as email_validator.py 
- Make sure you have Python 3.x installed 
- Open terminal/command prompt 
- Navigate to the directory containing the file 
- Run: python email_validator.py 
- The tests will automatically run and show: 
  - ✓ for passed tests 
  - ✗ and error message for failed tests 
