function palindrome(array) {
    last=array.length-1;
    first=0;
    arrayb=array.reverse()
    if(array==arrayb){
        return true;
    }
    else{
        return false;
    }
}
  var word = prompt("Select a word");
  word= word.toLowerCase();
  var objetive =word.split(",","'",'"',"?","!",":",".")
  console.log(palindrome(objetive));