'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countApplesAndOranges function below.
function countApplesAndOranges(s, t, a, b, apples, oranges) {
    //s its the frist house range
    // t its the last range of house
    //a its the apple tree
    //b its the orange tree
    //m is apples quantity
    //n is orange quantity
    let apple_in_house=0;
    let oranges_in_house=0;
    function inrange(s,t,input)
    {
        if(input>s || input<t)
        {
            return true;
        }else
        {
            return false;
        }
    }
    for (let i=0;i<apples.lenght;i++)
    {
        if(inrange(s,t,apples[i]))
        {
            apple_in_house=apple_in_house+1;
        }
    }
    for (let i=0;i<oranges.lenght;i++)
    {
        if(inrange(s,t,oranges[i]))
        {
            oranges_in_house=oranges_in_house+1;
        }
    }
    console.log(apples_in_house);
    console.log(oranges_in_house);
}

function main() {
    const st = readLine().split(' ');

    const s = parseInt(st[0], 10);

    const t = parseInt(st[1], 10);

    const ab = readLine().split(' ');

    const a = parseInt(ab[0], 10);

    const b = parseInt(ab[1], 10);

    const mn = readLine().split(' ');

    const m = parseInt(mn[0], 10);

    const n = parseInt(mn[1], 10);

    const apples = readLine().split(' ').map(applesTemp => parseInt(applesTemp, 10));

    const oranges = readLine().split(' ').map(orangesTemp => parseInt(orangesTemp, 10));

    countApplesAndOranges(s, t, a, b, apples, oranges);
}