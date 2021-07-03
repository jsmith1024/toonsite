function index(action, length = 0)
{
    alert("Inside of closure: " + action + " " + length);
    let index       = length;
    let last        = length;
    
    if(action === "first")
    {
        return function()
        {
            index   = 1;
            return index;
        }
    }
    else if(action === "previous")
    {
        return function()
        {
            index  -= 1;
            return index;
        }
    }
    else if(action === "reload")
    {
        return function()
        {
            return index;
        }
    }
    else if(action === "next")
    {
        return function()
        {
            index  += 1;
            return index;
        }
    }
    else if(action === "last")
    {
//                 alert("last");
        return function()
        {
            index   = last;
            return index;
        }
    }
    else
    {
        alert("YOU MESSED UP!!");
    }

};
