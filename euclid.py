#!/usr/bin/python

# Euclid's algorithm for greatest common divisor
# Euclid's rule: gcd(x,y) = gcd(x mod y, y)

def euclid_gcd (a, b):
    # Input: Two integers a and b, a >= b >= 0
    # Output: gcd(a,b)

    if b == 0:
        return a

    print (a, b, a % b)

    return euclid_gcd(b, a % b)



x = 201
y = 111

result = euclid_gcd(x, y)

print x, y, result

#(a,b,a%b)
#(201, 111, 90)
#(111, 90, 21)
#(90, 21, 6)
#(21, 6, 3)
#(6, 3, 0)

#201 111 3
