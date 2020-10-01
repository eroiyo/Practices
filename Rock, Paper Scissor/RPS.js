function victory(Pscore, PCscore)
{
    if (Pscore> PCscore)
    {
        return "VICTORY FOR HUMAN";
    }
    if(Pscore< PCscore)
    {
        return "VICTORY FOR COMPUTER";
    }
    if(Pscore==PCscore)
    {
        return "TIE";
    }
}
function computerplay(){

 number=Math.floor((Math.random() * 3) + 1);
 return number;
}
function humanplay(){
    let valid=false;
    while(valid==false){
    let input=prompt("Input Rock, Paper or Scissor");
    input= input.toUpperCase();
    if(input == "ROCK" || input == "PAPER" || input == "SCISSOR")
    {
        valid=true;
        return input;
    }else{
        console.log("Invalid input");
    }

}
}
function PlayRound(human,computer)
{
if(human=="ROCK"){
    human=1;
}
if(human=="PAPER"){
    return 2;
}
if(human=="SCISSOR"){
    return 3;
}
if(human==computer)
{
    console.log("Equal");
    Pscore++;
    PCscore++;
    return true;
}else{
    if(human % 2 ==0)
    {
        if(human>computer)
        {
            console.log('Paper beats Rock, Score for Human');
            return true;
        }else{
            console.log('Paper loses against Scissor, Score for Computer');
            return false;
        }
    }else{
        if(human!=3){
            if(computer==3)
            {
                console.log('Rock beats Scissor, Score for Human');
                return true;
            }else{
                console.log('Rock loses against Paper, Score for Computer');
                return false;
            }
        }else{
            if(human==2)
            {
                console.log('Scissor beats paper, Score for Human');
                return true;
            }
            else{
                console.log('Scissor loses against rocks, Score for Computer');
                return false;
            }
        }
    }
}
}
let s_start=0;
var Pscore =0;
var PCscore=0;
while(s_start!=5)
{
   let input=humanplay();
   let enemy=computerplay();
   let a = PlayRound(input,enemy);
   if(a==true)
   {
       Pscore++;
   }else
   {
       PCscore++;
   }
   s_start++;
}
console.log(victory(Pscore, PCscore));
