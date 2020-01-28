#!/usr/bin/python

# Modular Exponentiation, an iterative algorithm, cost is O(n^3)

def modexp_iterative (x, y, N):
    # Input: Two positive integers x and N, a non-negative integer exponent y
    # Output: x^y mod N
    

    if y == 0:
        return 1
    
    power = x 
    z=1
    
    while y > 0:
        digit = y % 2
        if digit == 1:
            z = power * z % N
        print(digit, power, z) # runtime check
    
        y = y // 2 # floor or y/2
        power = power ** 2 % N
        
        if power == 1:
            break  # z fixed

    return z

result = modexp_iterative(5,23, 61)
# you can test this in python: pow(5,23)%61
print "5^23 mod 61 =", result

