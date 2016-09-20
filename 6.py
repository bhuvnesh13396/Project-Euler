def sum_of_square():
    sum1=[x**2 for x in range(101)]
    ret=sum(sum1)
    
    return ret

def square_of_sum():
    sum1=[x for x in range(101)]
    ret=sum(sum1)
    
    return ret**2

print abs(sum_of_square() - square_of_sum() )

