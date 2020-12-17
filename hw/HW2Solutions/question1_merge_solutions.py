def merge2(I1, I2):          # Normal people
    result = []
    if len(I1) > len(I2):   # Determine smaller size one
        loops = len(I2)
    else:
        loops = len(I1)
    
    for i in range(loops):  # alternately
        result.append(I1[i])
        result.append(I2[i])
    
    if loops == len(I1):    # Add remaining
        result.extend(I2[loops:])
    else:
        result.extend(I1[loops:])
    return result


print([i for i in merge("what",range(100,105))])
print([i for i in merge(range(5),range(100,101))])
print([i for i in merge(range(1),range(100,105))])
