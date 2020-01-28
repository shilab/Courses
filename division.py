#!/usr/bin/python

# An algorithm for division, cost O(n^2)

def division (x, y):
    # Input: Two integers x and y with y >= 1
    # Output: (q, r) where q and r are the quotient and remainder of x divided by y

    if x == 0:
        return (0,0)

    (q, r) = division(x // 2, y)
    q = 2 * q
    r = 2 * r

    if x % 2: # if x is odd
        r = r + 1
    
    if r >= y:
        r = r - y
        q = q + 1

    return (q, r)


x = 201
y = 111

result = division(x, y)

print x, y, result

