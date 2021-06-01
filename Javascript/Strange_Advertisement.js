function viralAdvertising(day) {
    let shared=5;  
    let liked=0;  
    let comulative=0;  
    for(let i=0;i<day;i++)  
    {
        liked=shared/2;    
        liked=Math.floor(liked); 
        shared=liked*3; 
        comulative=comulative+liked;   
    }
    return comulative;
}