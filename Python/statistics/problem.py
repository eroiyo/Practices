def to_float(array):
    result=[]
    for x in array:
        x=float(x)
        result.append(x)
    result.sort()
    return result


string=input()
arr=string.split(' ')
arr=to_float(arr)

x=arr[0]
a=160+40*(x + pow(x,2))
y=arr[1]
b=128+40*(y+ pow(y,2))
print(a)
print(b)