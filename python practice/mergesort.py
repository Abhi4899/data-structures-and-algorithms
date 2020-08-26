n=int(input())
unsorted=[]
for i in range(n):
    num=int(input())
    unsorted.append(num)
def Merge(B,C):
    D=[]
    i=0
    j=0
    k=0
    while len(B)!=0 and len(C)!=0:
        b=B[0]
        c=C[0]
        if b<=c:
            D.append(b)
            B=B[1:]
        else:
            D.append(c)
            C=C[1:]
    D=D+B+C
    return D
def MergeSort(A):
    if len(A)<2:
        return A
    m=len(A)//2
    B=MergeSort(A[:m])
    C=MergeSort(A[m:])
    A1=Merge(B,C)
    return A1
sortedelements=MergeSort(unsorted)
for element in sortedelements:
    print(element)
