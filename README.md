# Problem 6
- This is an email validator that uses a state machine to check if an email address is valid 
- The validator checks for proper format: username@domain.tld (e.g., user@example.com) 
- The code includes both the validator class and unit tests to verify it works correctly 
- It checks for common email rules like: 
  - Valid characters in username (letters, numbers, ., _, -) 
  - Valid characters in domain (letters, numbers, -) 
  - Proper TLD length (must be 2+ characters) 
  - Proper placement of special characters 
