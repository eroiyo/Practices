function anagram (arraya, arrayb)
{
  if(arraya.length==arrayb.length){
    var sum_a=0;
    var sum_b=0;
    sum_a=get_value(arraya);
    console.log(sum_a)
    sum_b=get_value(arrayb);
    console.log(sum_b)

    if(sum_a==sum_b){
        return true;
    }else{
    return false;
    }
  }
  else{
  return false;
  }
}
var word = prompt("Select a word");
word= word.toLowerCase();
var objetive =word.split('')
var wordb = prompt("Select other word");
word= wordb.toLowerCase();
var objetiveb =word.split('')
console.log(anagram(objetive, objetiveb))