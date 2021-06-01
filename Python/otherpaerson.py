def to_float(array):
    result=[]
    for x in array:
        if(len(x)>0):
            x=float(x)
            round(x,3)
            result.append(x)
    result.sort()
    return result

N=int(input())
string=input()
arra=string.split(' ')
arra=to_float(arra)

string=input()
arrb=string.split(' ')
arrb=to_float(arrb)

mu_x = sum(arra) / N
mu_y = sum(arrb) / N

stdv_x = (sum([(i - mu_x)**2 for i in arra]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in arrb]) / N)**0.5


covariance = sum([(arra[i] - mu_x) * (arrb[i] -mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))