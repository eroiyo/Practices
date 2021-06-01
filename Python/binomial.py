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

def binomial(array,experiments,succes):
    n=(arr[0])
    odd= float(arr[1])
    
    fails=experiments-succes
    probability=probality_from_odds(odd)
    inverse=1-probability
    a=combinatory(experiments,succes)
    b= pow(probability,succes)
    c= pow(inverse,fails)
    return(a*b*c)

string=input()
arr=string.split(' ')
arr=to_float(arr)
print(binomial(arr,6,3))
