primes=[True for i in range(1000008)]
prime_no=[]

def sieve():
    primes[0]=False
    primes[1]=False
    
    for i in range(2,1000000):
        if primes[i]:
            prime_no.append(i)
            if len(prime_no) == 10001:break
            for j in range(i+i,1000000,i):
                primes[j]=False
                
sieve()              
print prime_no[-1]
