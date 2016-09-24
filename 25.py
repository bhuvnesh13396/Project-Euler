# fib_length stores the length of digit of i'th fibonacci number

fib_length=[1,1]
def fibo(n):
    a=1
    b=1
    for i in xrange(n):
        c=a+b
        fib_length.append(len(str(c)))
        if fib_length[-1]>=1000: break
        a=b
        b=c
        
fibo(10000)
print len(fib_length)
    
