def power(x,n):
    if n==0:
        return 1
    elif n==-1:
        return 1/x
    else:
        partial = power(x,n//2)
        result = partial*partial
        if n%2==1:
            result*=x
        return result

#print(power(-2, 4))
#print(power(4, 3))

#print(power(-2, -3))    # -0.125
#print(power(4, 3))      # 64