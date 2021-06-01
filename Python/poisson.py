import math
def to_float(array):
    result=[]
    for x in array:
        x=float(x)
        result.append(x)
    result.sort()
    return result

def permutation(number):
    result=[]
    true_result=1
    while number>0:
        result.append(number)
        number=number-1
    for e in result:
        true_result=true_result*e
    return true_result

def combinatory(n,x):
    n_permutation=permutation(n)
    x_permutation=permutation(x)
    n_minus_x_permutation=permutation(n-x)
    r_combinatory=n_permutation/(x_permutation*n_minus_x_permutation)
    return r_combinatory

def poissond(x,y):
    e=math.e
    e=pow(e,-(x))
    b=pow(x,y)
    result=(e*b)/permutation(y)
    return result



x=float(input())
y=float(input())

print ("%5.3f" %(poissond(x,y)))