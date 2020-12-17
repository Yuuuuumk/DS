#Problem5
def is_min_heap(array):
    for i in range(len(array) // 2):
        if 2 * i + 1 < len(array) and array[2 * i + 1] < array[i]:
            return False
        if 2 * i + 2 < len(array) and array[2 * i + 2] < array[i]:
            return False
    return True    

#test case
print(is_min_heap([9, 15, 11, 25, 17, 20])) #True
print(is_min_heap([2, 4, 3, 6])) #True
print(is_min_heap([2, 1, 3, 6])) #False
