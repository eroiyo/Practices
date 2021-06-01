function petition(){
    console.log("hi");
    let valid=false;
    while (valid == false) 
    {
        let input=prompt("Select Rock, Paper or Scissors"); //or something like thats
        input=input.toUpperCase();
        if(input == "ROCK" || input == "PAPER" || input == "SCISSORS") 
        {
            return input
        }
        else
        {
            console.log("invalid input") 
        }
        //artificial change
}
}
function check() {
    number=Math.floor(Math.random() * 3) ;
    if (number == 0 ) {
        return "ROCK"
    }
    else if (number == 1){
        return "SCISSOR"
    }
    else if (number ==2) {
        return "PAPER"
    }
}
function petition(){
    console.log("hi");
    let valid=false;
    while (valid == false) 
    {
        let input=prompt("Select Rock, Paper or Scissor"); //or something like thats
        input=input.toUpperCase();
        if(input == "ROCK" || input == "PAPER" || input == "SCISSOR") 
        {
            return input
        }
        else
        {
            console.log("invalid input") 
        }
}
}
function comparation(user_input,computer_input) {
    if(user_input==computer_input)// incase both are equal
    return "TIE"
    if (user_input=="SCISSOR")//incase you use scissor 
    {
        if (computer_input=="ROCK") 
        {return "LOSE"
        }
        else //scissors beat paper
        {
            return "WIN"
        }
    }
    if (user_input=="ROCK") //incase you use rock
    {
        if (computer_input=="PAPER") 
        {
            return "LOSE"
        }
        else //rock beats scissors
        {
            return "WIN"
        }
    }
     if (user_input=="PAPER") //incase you use paper
     {
         if (computer_input=="SCISSOR") 
         {
             return "LOSE"
         }
         else //paper beats scissors
         {
             return "WIN"
         }
     }   
    }
    {
}
let x = 0;
let repeat=5;
user_score=0;
computer_score=0;
while(x<repeat)
{
let user_input= petition()
let computer_input=check()
let result=comparation(user_input,computer_input)
if(result=="WIN"){user_score=user_score+1}
if(result=="LOSE"){computer_score=computer_score+1}
x++;
}

if(user_score>computer_score)
{
    console.log("The Player is the Winner")
}
if(user_score<computer_score)
{
    console.log("The Computer is the Winner")
}
if(user_score==computer_score)
{
    console.log("Its a Tie")
}