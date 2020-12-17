def unique(s):
    l = len(s)
    if l <= 1:
        return True
    elif not unique(s[:-1]):
        return False
    else:
        return not (s[-1] in s[:-1])


#print(unique([9,4,3,2,1,8]) )

#print(unique([1,7,6,5,4,3,1]))    # False
#print(unique([9,4,3,2,1,8]) )     # True
