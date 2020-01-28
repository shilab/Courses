import time

inputn=int(input("Please enter a number:"))
start = time.time()
def fac(n):
    prod = 1
    if n == 0:
        prod = 1
    else:
        for k in range(1,n+1):
            prod = prod * k
    return prod

end = time.time()

print(fac(inputn))
print("Time used: %.10f" % (end - start))

