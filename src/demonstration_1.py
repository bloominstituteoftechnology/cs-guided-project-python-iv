"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    res = ""

    for ch in string: 
        number = ord(ch)

        # Add 32 to num if it falls within this range
        if number >= 65 AND number <= 90:
            number += 32
        
        res += chr(number)

    return res

print(to_lower_case("LambdaSchool"))
print(to_lower_case("austen"))
print(to_lower_case("LLAMA"))
