'''This kata is to practice simple string output. Jamie is a programmer, and girlfriend of James. She likes diamonds, and this time she expects String of diamond from James. As James doesn't know how to do it, he needs your help.

Task:

You need to print a shape on the screen using asterisk ("*") characters.

The shape that will be returned from print method resembles a diamond, where the number provided as input represents the number of *’s printed on the middle line. The line above and below will be centered and will have 2 less *’s than the middle line. This reduction by 2 *’s for each line continues until a line with a single * is printed at the top and bottom of the figure.

Return null if input is even number (as it is not possible to print diamond with even number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python, Python students must implement the diamond(n) method instead, and return None for invalid input.

JS Note

JS students, like Python ones, must implement the diamond(n) method, and return null for invalid input.
'''


import math

def diamond(n):
    if(n%2 == 0 or n < 3):
        return None
    space = int(math.floor(n/2))
    num = n
    gone = False
    ans = ""
    while num > 0:
        str = " " * int(space)
        star = "*" * (n - (int(space)*2)) + "\n" 
        ans += str  + star
        num -= 1
        if(space == 0):
            gone = True
        else:
            if(gone != True):
                space -= 1
        if (gone == True):
            space += 1
    # Make some diamonds!
    return ans


'''def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None'''