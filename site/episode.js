var episode             = {};

episode.index           = 0;

episode.first           = function()
{
    if(!(null === length))
    {
        episode.index   = 1;
    }
}

episode.previous        = function()
{
    if(!(null === length) && (episode.index > 1))
    {
        episode.index  -= 1;
    }
}

episode.next            = function()
{
    if(!(null === length) && (episode.index < (length - 1)))
    {
        episode.index  += 1;
    }
}

episode.last            = function()
{
    
    if(!(null === length))
    {
        episode.index   = length - 1;
    }
}
