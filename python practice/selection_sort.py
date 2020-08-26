

def swap(a,b):
    c=a
    a=b
    b=c
    return (a,b)

def selectionSort(l):
    for i in range(len(l)):
        minIndex=i
        for j in range(i+1,len(l)):
            if l[j]<l[minIndex]:
                minIndex=j
        l[i],l[minIndex]=swap(l[i],l[minIndex])
    return l

s=input('Enter list of nos seperated by space\n')
lst=[int(x) for x in s.split()]
print(selectionSort(lst))
