DFA Rules
A string is accepted if:

The absolute difference between the number of 'a's and 'b's is ≤ 3
|nₐ - nᵦ| ≤ 3 where:

nₐ is the count of 'a's
nᵦ is the count of 'b's



Modifying Test Strings
To test different strings:

Open dfa_simulator.py in a text editor
Modify the test_strings list
Save and run the program again

Example Output
CopyString Testing Results:
----------------------------------------
Input String              | Result
----------------------------------------
aaa                      | Accept
abab                     | Accept
...
Error Handling
The program assumes all input strings contain only 'a' and 'b' characters. For other characters, modify the simulator function accordingly.
