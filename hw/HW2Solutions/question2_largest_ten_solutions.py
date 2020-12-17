import sys
def largest_ten(l):

    # Assuming list size greater than 10
    largest_indexes = [None] * 10       # Store largest 10 index
    for i in range(10):
        local_max = -sys.maxsize        # Start from negative infinity, search for largest
        local_max_index = None
        for j in range(len(l)):
            if j in largest_indexes:    # Skip stored indexes
                pass
            else:
                if (l[j] > local_max):
                    local_max = l[j]
                    local_max_index = j
        largest_indexes[i] = local_max_index
        
    return [l[x] for x in largest_indexes]      # Runtime O(10n) = O(n)


print(largest_ten([9,8,6,4,22,68,96,212,52,12,6,8,99]))
    
