def sumOfList(l):
    if len(l)==1:
        return l[0]
    return l[0]+sumOfList(l[1:])

s=input('Enter space seperated numbers\n')

lst=[int(x) for x in s.split()]

print('Sum =',sumOfList(lst))
