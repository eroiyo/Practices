// Complete the breakingRecords function below.
function breakingRecords(scores) {
    let minimun_record=scores[0];
    let maximun_record=scores[0];
    let max=0;
    let min=0;

    for(let i=0;i<scores.length; i++)
    {
        if(scores[i]>maximun_record)
        {
            maximun_record=scores[i];
            max=max+1;}
        if(scores[i]<minimun_record)
        {
            minimun_record=scores[i];
            min=min+1;}
    }
    let record=[max,min]
    return record;

}