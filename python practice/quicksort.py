import random

def quicksort(lst):
    if len(lst)<2:
        return lst
    else:
        pi=random.randint(0,len(lst)-1)
        pivot=lst[pi]
        less=[i for i in lst if i<pivot]
        mid=[i for i in lst if i==pivot]
        big=[i for i in lst if i>pivot]
        return quicksort(less)+mid+quicksort(big)

s=input('Enter space seperated numbers\n')

l=[int(x) for x in s.split()]

print(*quicksort(l),sep=' ')
