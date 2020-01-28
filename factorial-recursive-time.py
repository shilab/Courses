import time

inputn=int(input("Please enter a number:"))
start = time.time()
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1) 
end = time.time()

print(fac(inputn))
print ("Time used: %.10f" % (end - start))

