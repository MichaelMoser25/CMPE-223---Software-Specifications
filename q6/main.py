""" CMPE 223 - Software Specifications
Problem 6:
Write a code to validate email addresses using a state machine approach. 
Implement a function that determines email validity based on state transitions, 
where the local part can contain letters, dots, hyphens, and underscores, and the 
domain part must contain letters with a dot followed by additional letters. 
Create a test suite with at least 5 different email inputs to demonstrate the 
validation logic.

"""

from enum import Enum
import unittest


class State(Enum):
    START = 0       # initial state before validation begins
    LOCAL = 1       # Processing local part before @ (username)
    AT = 2          # Found @ symbol
    DOMAIN = 3      # Processing domain name
    DOT = 4         # Foun . after domain
    TLD = 5         # Processing top-level domain (com, org, etc)
    VALID = 6       # Email passed all validation
    INVALID = 7     # Email failed validation 

class EmailValidator:
    def __init__(self):
        # Set inital state to 0 --- START(0)
        self.state = State.START
        # define allowed characters before  @ (letters, numbers, ., _, -)
        self.valid_local_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-')
        # define allowed characters in domain (letters, numbers, -)
        self.valid_domain_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
        # Counter to track top-level domain length (must be >= 2)
        self.tld_length = 0

        """ EXAMPLE CASE
        test@gmail.com
        Local --> "test"
        Domain --> "gmail"
        TLD --> "com"
        """

    def validate(self, email: str) -> bool:
        self.state = State.START
        self.tld_length = 0

        """
        The state machine transitions through these states in sequence:
        START -> LOCAL -> AT -> DOMAIN -> DOT -> TLD
        """

        # Loop through each character
        for i, char in enumerate(email):
            # Start state, begining of email address
            if self.state == State.START:
                if char in self.valid_local_chars and char not in '._-':
                    # Character is VALID
                    self.state = State.LOCAL
                else:
                    # Character is INVALID
                    self.state = State.INVALID
                    break   # EXIT LOOP
                    
            elif self.state == State.LOCAL:
                # Found @ symbol
                if char == '@':
                    self.state = State.AT
                # INVALID character
                elif char not in self.valid_local_chars:
                    self.state = State.INVALID
                    break
                # VALID character
                elif char in '._-' and (i == len(email)-1 or email[i+1] in '._-@'):
                    self.state = State.INVALID
                    break
                    
            elif self.state == State.AT:
                if char in self.valid_domain_chars and char not in '-':
                    # VALID character and not hyphen
                    self.state = State.DOMAIN
                else:
                    # INVALID character after @
                    self.state = State.INVALID
                    break
                    
            elif self.state == State.DOMAIN:
                # found . after domain
                if char == '.':
                    self.state = State.DOT
                # INVLAID domain character
                elif char not in self.valid_domain_chars:
                    self.state = State.INVALID
                    break
                    
            elif self.state == State.DOT:
                # TLD must start with a letter
                if char.isalpha():
                    # Move TLD state
                    self.state = State.TLD
                    # Count TLD length
                    self.tld_length = 1
                else:
                    # INVLAID TLD start .... number or special character
                    self.state = State.INVALID
                    break
                    
            elif self.state == State.TLD:
                # Found another dot (e.g , .co.uk)
                if char == '.':# TLD must be 2+ chars
                    if self.tld_length < 2:
                        self.state = State.INVALID
                        break
                    # Reset to DOT state for nect segment
                    self.state = State.DOT
                # VALID letter in TLD
                elif char.isalpha():
                    # increment TLD length
                    self.tld_length += 1
                # INVALID TLD
                else:
                    self.state = State.INVALID
                    break

        # Finally Check validity 
        if self.state == State.TLD and self.tld_length < 2:
            self.state = State.INVALID
        elif self.state == State.TLD:
            self.state = State.VALID
            
        return self.state == State.VALID

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()
        
    def test_valid_emails(self):
        valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "user-name@domain.org",
            "user_name@domain.net",
            "a@b.com"
        ]
        for email in valid_emails:
            self.assertTrue(self.validator.validate(email), f"Failed to validate {email}")
            
    def test_invalid_emails(self):
        invalid_emails = [
            "@domain.com",
            "user@.com",
            "user@domain.",
            "user..name@domain.com",
            "user@domain..com",
            "user.@domain.com",
            ".user@domain.com",
            "user-@domain.com",
            "user@-domain.com",
            "user@domain.c",
            "user@domain@com",
            "user@domain.123"
        ]
        for email in invalid_emails:
            self.assertFalse(self.validator.validate(email), f"Should not validate {email}")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
