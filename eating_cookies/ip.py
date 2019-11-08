def e(n):
    count = 0
    def eat(n,x):
        nonlocal count
        s = n-x
        if s==0:
            count +=1
        elif s<0:
            pass
        else:
            eat(s,3) 
            eat(s,2)
            eat(s,1)
    eat(n,0)
    return count
e(3)

