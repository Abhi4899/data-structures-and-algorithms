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

def strToList(st):
    l=[int(x) for x in st.split()]
    return l

s=input()
bEl=strToList(s)
s=input()
cEl=strToList(s)

print(Merge(bEl,cEl))
