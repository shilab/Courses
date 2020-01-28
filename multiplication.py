#!/usr/bin/python

# An algorithm for multiplication

def multiplication (x, y):
    # Input: Two integers x and y with y >= 0
    # Output: The product of x and y

    if y == 0:
        return 0

    z = multiplication (x, y // 2)
#    z = multiplication (x, y >> 1) # right shift by 1 : divide by 2
    

    if y % 2 == 0: # if x is even
#    if x & 1 == 0:
        return 2*z
    else:
        return x + 2*z


x = 201
y = 111

result = multiplication(x, y)

print x, y, result

# the cost is O(n^2)
