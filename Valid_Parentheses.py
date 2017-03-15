"""
Write a function called validParentheses that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
validParentheses should return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 

All input strings will be nonempty, and will only consist of 
open parentheses '(' and/or closed parentheses ')'

"""

def valid_parentheses(string):
    string = ''.join([s for s in string if s == '(' or s == ')'])
    s = []
    for a in string:
        if a == "(":
            s.append(a)
        else:
            if len(s) == 0:
                return False
            elif s.pop() != "(":
                return False
    if(len(s) != 0) :
        return False
    return True


"""
Best Practices:

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

"""