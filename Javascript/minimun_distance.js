// Carlos Arturo Ortega: but first let me explain

//we have Array A the one the exercise give us

//Array B, the array we will create to save all the minimun distances (the results)

 //we will do a loop in the first array for every position to find a clone
 //if there is a clone, we break the loop, and we put the result in the array B
 //after that we do a loop in the array b to look for the smallest distance

function minimumDistances(a) {
    arrayb=[a.length+1];                  // array where we save all the information
    for(let c=0; i<a.length; c++){       //loop to do loops for every postiion
        for (let i =c+1; i<a.length; i++ ){  //individual loops
            if (a[i]==a[c]){             //if two values are the same, we get the distance
                arrayb.push(c-i)          //and save it in the result arrays
                break;
            }
        }
    }
    if(arrayb.length>1)                   //if the result array if filled we will search the lowest value
    {
        result=10000;
        for(let i=0; i<arrayb.length; i++)  //loop for every element
        {
            if(result>arrayb[i]){              //if the value is lowest
                result=arrayb[i];             //we save it
            }
        }
        return result;
    }
    return (-1)                              //its the array i'ts not filled we return -1
}

