def pascal(n):
    if n ==1:
        return [[1]]
    else:
        newline = [1]
        for i in range(n-2):
            ele = pascal(n-1)[n-2][i]+pascal(n-1)[n-2][i+1]
            newline.append(ele)
        newline.append(1)
        return pascal(n-1)+[newline]



#print(pascal(1))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]