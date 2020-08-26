def inv(arr):
    i=1
    flag=0
    count=0
    while i<len(arr):
        j=i
        while j>0:
            if arr[j]<arr[j-1]:
                c=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=c
                flag=1
            j=j-1
        i+=1
        
        if flag==1:
            count+=1
            flag=0
    return count
n=int(input())
s=input()
l=[int(x) for x in s.split()]
print(inv(l))


