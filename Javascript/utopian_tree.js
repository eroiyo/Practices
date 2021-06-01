// Complete the utopianTree function below.
function utopianTree(n) {
    let summer=false
    let height=1;
    for (let i =0;i<n;i++)
    {
        if(summer)
        {
            height=height+1
            summer=false;
        }else
        {
            height=height*2;
            summer=true;
        }
    }
    return height;
    


}