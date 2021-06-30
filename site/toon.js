var toon        = {};

toon.index      = 0;

toon.first      = function()
{
//     if(!(null === series))
//     {
        toon.index  = 1;
//     }
}

toon.previous   = function()
{
//     if(!(null === series) && (index > 1))
//     {
        toon.index -= 1;
//     }
}

toon.next   = function()
{
//     if(!(null === series) && (index < (length - 1)))
//     {
        toon.index += 1;
//     }
}

toon.last   = function()
{
    
//     if(!(null === series))
//     {
        toon.index  = 3;
//     }
}
