function bonAppetit(bill, k, b) {
    let total=0;                      
    for(let i=0; i<bill.length;i++)
    {
        if(i==k)
        {//nothing
        }
        else
        {
            total=total+bill[i]
        }
        //this for calculate the total of the bill without the element k
    }
    let true_total=total/2   //the half of the total bill without the k price
    if(true_total==b)
    {
        console.log("Bon Appetit") //if anna money exactly the half of the bill
    }
    else{
        true_total=true_total-b
        if(true_total<0)
        {true_total=true_total*-1}
        console.log(true_total)        //else return difference
    }
}