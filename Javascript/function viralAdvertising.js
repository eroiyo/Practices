function viralAdvertising(day) {
    let shared=5;
    let cumulative=0;
    let half=0;
    for (i=0;i<day;i++)
    {
        half=shared/2;
        if (half%2!=0){ Math.floor(half=half-0.5)}
        shared=half*3;
        cumulative=cumulative+half;
        Math.round
        }
    return cumulative;


}