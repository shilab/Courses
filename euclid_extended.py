#!/usr/bin/python

# An extension of Euclid's algorithm for greatest common divisor

def euclid_extended (a, b):
    # Input: Two integers a and b, a >= b >= 0
    # Output: Integers x,y,d such that d = gcd(a,b) and ax + by = d

    if b == 0:
        return (1, 0, a)

    print (a, b, a % b)

    (x1, y1, d) = euclid_extended(b, a % b)
    return (y1, x1 - a //b * y1, d)



x = 201
y = 111

# result = (x, y, d)
(x,y,d) = euclid_extended(x, y)

print (x,y,d)

#(a,b,a%b)
#(201, 111, 90)
#(111, 90, 21)
#(90, 21, 6)
#(21, 6, 3)
#(6, 3, 0)

#(-16, 29, 3)
