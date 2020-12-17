def has_duplicate(list1):
    ### O(n^2) algorithm
    for each in list1:
    	if list1.count(each) > 1:
    		return True
    return False

