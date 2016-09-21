
def func():
    for a in xrange(1,1000):
        for b in xrange(a+1,1000):
            c=1000-a-b
            if c>a and c>b:
                if c**2==a**2+b**2:
                    return a*b*c
                
                
ans=func()
print ans
