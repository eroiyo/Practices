def median(input):
    index=len(input)/2
    if(len(input) %2 ==0):
        index=int(index)
        other_index=index-1
        true_result=(input[index]+input[other_index])/2
    else:
        round(index)
        true_result=input[index]
    return true_result

def quartily(arr,n):
    t=int(len(arr)/2)
    if len(arr)%2==0:
        L=arr[:t]
        U=arr[t:]
    else:
        L=arr[:t]
        U=arr[t+1:]
    print(int(median(L)))
    print(int(median(arr)))
    print(int(median(U)))


n=int(input())
string=input()
arr=str.split(' ')
arr.sort()
quartily(arr,n)