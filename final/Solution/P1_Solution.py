#Problem1
def print_missing(arr, low, high):
    d = {}
    for each in arr:
        d[each] = "whatever"
    
    for i in range(low, high):
        if i not in d:
            print(i, end=" ")
            
            
#test case1
arr = [10, 12, 11, 15]
low = 10
high = 15
print_missing(arr, low, high) #Output: 13, 14

#test case2   
arr = [1, 14, 11, 51, 15]
low = 50
high = 55
print_missing(arr, low, high) #Output: 50, 52, 53, 54



    
  
    









            
            
            
      
