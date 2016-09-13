arr=[]
for i in reversed(range(999)):
    for j in reversed(range(999)):
        s=i*j
        
        st=str(s)
        v=st[::-1]
        if v==st:
            arr.append(i*j)
            
print max(arr)
