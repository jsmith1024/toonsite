/* @file    events.js
 * @brief   Javascript functions to facilitate a comic strip  presentation website.
 * @authors j.smith and j. smith
 */

function addEventListeners()
{
    document.getElementById("first").addEventListener("click", function()
    {
//         alert("first");
        alert(toon.index);
        if(!(null === series))
        {
            episode.first();
        }
        update();
    });
    
    document.getElementById("previous").addEventListener("click", function()
    {
//         alert("first");
        alert(toon.index);
        if(!(null === series) && (index > 1))
        {
            episode.previous();
        }
        update();
    });
    
    document.getElementById("next").addEventListener("click", function()
    {
//         alert("first");
        alert(toon.index);
        if(!(null === series) && (index < (length - 1)))
        {
            episode.next();
        }
        update();
    });
    
    document.getElementById("last").addEventListener("click", function()
    {
//         alert("first");
        alert(toon.index);
        if(!(null === length))
    {
        episode.last();
    }
    update();
        update();
    });
}
