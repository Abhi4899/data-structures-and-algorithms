s=input()
l=[int(x) for x in s.split()]
sortedlst=[]
while len(l)>0:
    minIndex=l.index(min(l))
    sortedlst.append(l[minIndex])
    l=l[:minIndex]+l[minIndex+1:]
print(sortedlst)
    
