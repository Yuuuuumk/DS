import copy

def knapsack_driver(capacity, weights):
    '''
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information for recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    '''
    overall_combinations=[]
    helper_knapsack(capacity, weights, [], 0, overall_combinations)
    return overall_combinations

def helper_knapsack(capacity, list1, helper_list, index, overall_list):
    if sum(helper_list) == capacity:
        overall_list.append(helper_list)
        return
    elif index >= len(list1):
        return
    else:
        helper_list_copy = copy.deepcopy(helper_list)
        helper_list_copy.append(list1[index])
        helper_knapsack(capacity, list1, helper_list, index + 1, overall_list)
        helper_knapsack(capacity, list1, helper_list_copy, index + 1, overall_list)

def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    print(knapsack_driver(14, casts))  

if __name__ == '__main__':
    main()












