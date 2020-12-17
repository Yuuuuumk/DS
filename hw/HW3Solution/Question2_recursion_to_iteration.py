def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return 1 + recur(n // 10)

def iterative(n):
    result = 0
    if n < 0:
        return -1
    else:
        while n >= 10:
            result += 1
            n = n//10
        result += 1
    return result

