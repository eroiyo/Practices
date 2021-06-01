function hurdleRace(k, height) {
let potions=0;
for (i in height)
{
    if (i>k)
    {
        potions=potions+(i-k)
        k=i;
    }
}
return potions;

}