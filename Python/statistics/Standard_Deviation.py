import math
def my_median(sample):
    n = len(sample)
    index = n // 2
    if n % 2:
        return sorted(sample)[index]
    return sum(sorted(sample)[index - 1:index + 1]) / 2
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
    print("{0:.1f}".format(total))
n=input()
string=input()
arr=string.split(' ')
arr=to_integer(arr)
stan_deviation(arr)