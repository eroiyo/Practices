function palindrome(array) {
    last=array.length-1;
    first=0;
    result=true;
    while(first<=last)
    {
      if(array[first]!=array[last]){
        return false
      }
      first=first+1
      last=last-1;
    }
    return true;
  }
  var word = prompt("Select a word");
  word= word.toLowerCase();
  var objetive =word.split('')
  console.log(palindrome(objetive));