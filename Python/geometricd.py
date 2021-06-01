def to_float(array):
    result=[]
    for x in array:
        x=float(x)
        result.append(x)
    result.sort()
    return result
def geometricd(p,n):
    inverse=1-p
    return(p*(pow(inverse,(n-1))))


string=input()
arr=string.split(' ')
arr=to_float(arr)
p=float(arr[0]/arr[1])
n=float(input())
inverse=1-p

print("%5.3f" %(geometricd(inverse,n)))
