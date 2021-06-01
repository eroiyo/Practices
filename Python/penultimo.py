if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    def whatever(arr,n):
        ordened= sorted(arr, reverse = True)
        x=ordened[0];
        y=0;
        for i in ordened:
            if(i==x):
            
                continue;
            else:
                y=i;
                return y;


        return x;
print(whatever(arr,n));
