import time

inputn=int(input("Please enter a number:"))
start = time.time()
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
end = time.time()

print(fib1(inputn))
print ("Time used: %10.10f" % (end - start))

