import time

inputn=int(input("Please enter a number:"))
start = time.time()
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
end = time.time()

print(fib(inputn))
print ("Time used: %10.10f" % (end - start))

