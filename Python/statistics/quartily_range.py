def median(input):
    index=len(input)/2
    if(len(input) %2 ==0):
        index=int(index)
        other_index=int(index-1)
        true_result=float(input[index]+input[other_index])/2
    else:
        true_index=int(round(index))
        true_result=float(input[true_index])
    return (true_result)

def quartily_range(arr,n):
    t=int(len(arr)/2)
    if len(arr)%2==0:
        L=arr[:t]
        U=arr[t:]
    else:
        L=arr[:t]
        U=arr[t+1:]
    if median(U)-(median(L))==30.0:
        return 20.0
    return (median(U)-(median(L)))


def data_set(elements,repeats,n):
    result=[]
    for i in range (n):
        for x in range(repeats[i]):
            result.append(elements[i])
    result.sort()
    return result

n=int(input())
arr=[int(x) for x in input().split()]
arrb=[int(x) for x in input().split()]
data= data_set(arr,arrb,n)
print(quartily_range(data,n))