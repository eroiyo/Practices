def to_float(array):
    result=[]
    for x in array:
        x=float(x)
        result.append(x)
    result.sort()
    return result

def probality_from_odds(odds):
    probability=float(odds/(1+odds))
    return probability

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

def binomial(p,n,x):
    fails=n-x
    inverse=1-p
    return (combinatory(n,x)  *pow(p,x)    *pow(inverse,fails))

string=input()
arr=string.split(' ')
arr=to_float(arr)
inverse=float(arr[1]/100)
n=arr[0]
probability=1-inverse
probability0=binomial(probability,n,0)
probability1=binomial(probability,n,1)
probability2=binomial(probability,n,2)
probability3=binomial(probability,n,3)
probability4=binomial(probability,n,4)
probability5=binomial(probability,n,5)
probability6=binomial(probability,n,6)
probability7=binomial(probability,n,7)
probability8=binomial(probability,n,8)
probability9=binomial(probability,n,9)
probability10=binomial(probability,n,10)

inverse0=binomial(inverse,n,0)
inverse1=binomial(inverse,n,1)
inverse2=binomial(inverse,n,2)
inverse3=binomial(inverse,n,3)
inverse4=binomial(inverse,n,4)
inverse5=binomial(inverse,n,5)
inverse6=binomial(inverse,n,6)
inverse7=binomial(inverse,n,7)
inverse8=binomial(inverse,n,8)
inverse9=binomial(inverse,n,9)
inverse10=binomial(inverse,n,10)

print("%5.3f" %(inverse0+inverse1+inverse2))
print("%5.3f" %(inverse2+inverse3+inverse4+inverse5+inverse6+inverse7+inverse8+inverse9+inverse10))

