function miniMaxSum(arr) {
arr.sort();
let max=0;
let min=0;
for(let i=0; i<arr.lenght-2; i++)
{
    min=arr[i]+min;
}
for(let i=1; i<arr.lenght-1; i++)
{
    max=arr[i]+max;
}
console.log(min+" "+max);
}