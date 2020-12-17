"""
Assignment 1 question2 divide by 2 solutions
"""

def number_of_times_divideby2(n):
    """
    :param n: Int -- the input positive integer, greater than 2.

    :return: number of times one must repeatedly divide this number by 2 
             before getting a value less than 2.
    """
    # To do
    times = 0
    while n >= 2:
        n /= 2
        times += 1
    return times


