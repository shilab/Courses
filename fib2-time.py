import time

inputn=int(input("Please enter a number:"))
start = time.time()

# We can avoid the repeated work done is fib1 by storing the Fibonacci numbers calculated so far.

def fib2(n):

    fibArray = [0,1]

    while len(fibArray) < n+1:
        fibArray.append(0)

    if n <= 1:
        return n
    else:
        if fibArray[n-1] == 0:
            fibArray[n-1] = fib2(n-1)
        if fibArray[n-2] == 0:
            fibArray[n-1] = fib2(n-2)
    fibArray[n] = fibArray[n-2] + fibArray[n-1]
    return fibArray[n]
end = time.time()

print(fib2(inputn))
print ("Time used: %10.10f" % (end - start))

