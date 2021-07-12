fibonacci(num)
{
    var before=0;
    var present=1;
    var next=0;
    var sum=0;

    for(present;present<num;)
    {
        next=present+before;
        before=present;
        if(present % 2 !==0){
            sum+=present;
            present=next;
        }
    }
    return sum;
}
module.exports = repeatStringNumTimes
//forced pull request 2
