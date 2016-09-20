primes=[True for i in range(2000008)]
prime_no=[]
ans=0
def sieve():
    primes[0]=False
    primes[1]=False
    
    for i in range(2,2000000):
        if primes[i]:
            prime_no.append(i)
            for j in range(i+i,2000000,i):
                primes[j]=False
                
sieve()              
print sum(prime_no)
                

    
#
