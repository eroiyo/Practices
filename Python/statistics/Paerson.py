import math
def to_float(array):
    result=[]
    for x in array:
        x=float(x)
        round(x,3)
        result.append(x)
    result.sort()
    return result
def mean(input):
    mean=0
    for i in range(len(input)):
        value=input[i]
        mean=mean+value
    mean=mean/len(input)
    return round(mean,3)
def rest(input,mean):
    result=[]
    for i in range(len(input)):
        value=input[i]-mean
        result.append(value)
    return (result)

def my_median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        return sorted(sample)[index]
    return round((sum(sorted(sample)[index - 1:index + 1]) / 2),3)
def to_integer(array):
    result=[]
    for x in array:
        x=int(x)
        result.append(x)
    result.sort()
    return result
def mean(input):
    mean=0
    for i in range(len(input)):
        value=input[i]
        mean=mean+value
    mean=mean/len(input)
    return mean
    
def stan_deviation(array):
    the_median=float(mean(array))
    result=[]
    sum=0
    for x in array:
        y=(x-the_median)**2
        result.append(y)
    for x in result:
        sum=sum+x
    total=sum/len(array)
    total=math.sqrt(total)
    return float(total)
def covariance(arra,arrb,n):
    meana=mean(arra)
    z=float(n)-1
    meanb=mean(arrb)
    othera=rest(arra,meana)
    otherb=rest(arrb,meanb)
    last=0
    for i in range(len(arra)):
        value=arra[i]*arrb[i]
        last=value+last
    last=last/z
def paerson(arra,arrb,n):
    meana=mean(arra)
    meanb=mean(arrb)
    covariancex=covariance(arra,arrb,n)

    
n=input()
string=input()
arra=string.split(' ')
arra=to_float(arra)

string=input()
arrb=string.split(' ')
arrb=to_float(arrb)

print(covariance(arra,arrb,n))

print(round(mean(arra),3))
print(round(stan_deviation(arra),5))
print(round(mean(arrb),3))
print(round(stan_deviation(arrb),4))
