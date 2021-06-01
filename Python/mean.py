def mean(input):
    mean=0;
    for i in range(len(input)):
        value=input[i];
        mean=mean+value;
    mean=mean/len(input);
    return mean;

def mode(input):
    mode=input[0];
    old_subjet=input[0];
    mode_flag=1;
    subjet_flag=0;
    for elements in input:
        subjet=elements;
        if old_subjet==elements:
            subjet_flag=subjet_flag+1;
        else:
            old_subjet=subjet
            subjet_flag=1;
        if(mode_flag<subjet_flag):
            mode_flag=subjet_flag;
            mode=subjet;
    return mode;

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
if __name__ == '__main__':
    lenght=input();
    array=input();
    array = array.split(' ');
    for i in range(len(array)):
        integer=int(array[i]);
        array[i]=integer;
    array= sorted(array);
    n= mean(array);
    print(n);
    n= median(array);
    print(n);
    n= mode(array);
    print(n);