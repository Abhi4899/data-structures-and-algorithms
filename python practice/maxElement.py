def maximum(lst):
    if len(lst)==2:
        return lst[0] if lst[0]>=lst[1] else lst[1]
    submax=maximum(lst[1:])
    return lst[0] if lst[0]>submax else submax

print(maximum([2,7,21,9,100]))

    
