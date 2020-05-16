primeFactors = []
def prime_factors(n):
    primeFactors.append(1)
    i = 2
    while (i < n):
           if n%i == 0:
               primeFactors.append(i)
               n = n/i
           else:
                 i += 1
    primeFactors.append(n)

# test

n = 903746

prime_factors(n)
for i in range(len(primeFactors)):
    print(primeFactors[i])
    
