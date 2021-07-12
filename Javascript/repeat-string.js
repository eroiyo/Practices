function repeatStringNumTimes(str, num) {
    var response="";
    if(num>0){
    for(i=1;i<num;i++)
    {
        response+=str;
        console.log(str)
    }
    }else{
        console.log(response);
    }
    return response;

  }
  
  module.exports = repeatStringNumTimes
  