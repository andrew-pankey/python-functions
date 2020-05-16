import math



def is_prime(n):     #returns True if prime
    i=2
    while i<= math.sqrt(n):
        if n%i == 0:
            return (False)
        i+=1
    return (True)

# test
n=1111701
if is_prime(n)==True:
    print(n, "is prime")
else:
    print(n, " is not prime")


