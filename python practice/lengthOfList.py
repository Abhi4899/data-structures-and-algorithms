def length(l):
    if l==[]:
        return 0
    try:
        le=l[0]/l[0]
    except:
        le=1
    return int(le)+length(l[1:])

s=input('Enter space seperated numbers\n')

lst=[int(x) for x in s.split()]

print('length =',length(lst))
