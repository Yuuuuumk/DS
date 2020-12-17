def three_way_disjoint(l1, l2, l3):

    lissy = l1 + l2 + l3        # O(n)
    lissy.sort()                # O(nlogn)
    for i in range(len(lissy) - 1):   # O(n)
        if (lissy[i] == lissy[i + 1] == lissy[i + 2]):
            return False

    return True



l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10,11,12]
l3 = [5,13,14,15,16]
l4 = [5,6,7,8,9,10,11]

print(three_way_disjoint(l1,l2,l3))
print(three_way_disjoint(l1,l4,l3))
