#!/usr/bin/python

# Modular Exponentiation, a recursive algorithm

def modexp_recursive (x, y, N):
    # Input: Two positive integers x and N, a non-negative integer exponent y
    # Output: x^y mod N
    # 

    if y == 0:
        return 1
    
    z = modexp_recursive(x, y//2, N)

    print (x, y, z)
#    z = (z*z) % N
    
    if y%2 == 0: # y is even
        return (z*z) % N
    else:
        return (x*z*z) % N

result = modexp_recursive(5,23, 61)
# you can test this in python: pow(5,23)%61
print "5^23 mod 61 =", result

