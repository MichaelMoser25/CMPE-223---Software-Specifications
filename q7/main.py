def simulate_dfa(input_string):
    # States represent difference between count of a's and b's
    # All states from -3 to +3 are accepting states
    current_state = 0  # Initial state (no difference)
    
    for char in input_string:
        if char == 'a':
            current_state += 1
        elif char == 'b':
            current_state -= 1
            
        # If difference exceeds 3 in either direction, reject
        if abs(current_state) > 3:
            return False
            
    return True  # Accept if final difference is within bounds

# Test strings from the table
test_strings = [
    'aaa',
    'abab',
    'aaabbb',
    'aaaaaaa',
    'bbbbbbb',
    'aaaaaaaabbbbbbbb',
    'bbbb',
    'aaaabbbbaaaa',
    'bbbaaaabbbb',
    'aaaaaaaabbbbbbbb',
    'ababab',
    'abababab',
    'aaabbbba',
    'abbbaaaa',
    'bbbaaabbb',
    '',  # empty string
    'a',
    'b',
    'aaabbb',
    'abababababab'
]

# Test each string and print results
print("String Testing Results:")
print("-" * 40)
print("Input String".ljust(25) + "| Result")
print("-" * 40)

for s in test_strings:
    display_string = '(empty string)' if s == '' else s
    result = "Accept" if simulate_dfa(s) else "Reject"
    print(f"{display_string.ljust(25)}| {result}")
