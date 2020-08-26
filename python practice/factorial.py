def fact(x):
    if x==1:
        return x
    return x*fact(x-1)

n=int(input('Enter a number\n'))
print('{}! = {}'.format(n,fact(n)))
