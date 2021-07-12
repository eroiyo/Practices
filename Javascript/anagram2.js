function anagram (arraya, arrayb)
{
    var sum_a=0;
    var sum_b=0;
    sum_a=get_value(arraya);
    sum_b=get_value(arrayb);

    if(sum_a==sum_b){
        return true;
    }else{
    return false;
    }
}
function get_value(array){
    var sum=0;
    for(i=0; i<array.lenght; i++){
        sum=sum+array[i];
    }
    return sum;
}
var word = prompt("Select a word");
word= word.toLowerCase();
var objetive =word.split('')
var wordb = prompt("Select other word");
word= wordb.toLowerCase();
var objetiveb =word.split('')
console.log(anagram(objetive, objetiveb))