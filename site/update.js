/* @file    update.js
 * @brief   Javascript functions to facilitate a comic strip  presentation website.
 * @authors j.smith and j. smith
 */

/* last
 * @brief   update divs
 */
function update()
{
    if(null === series)
    {
        document.getElementById("title").innerHTML      = "<h1>Coming soon...</h1>";
        document.getElementById("first").disabled       = true;
        document.getElementById("previous").disabled    = true;
        document.getElementById("about").disabled       = true;
        document.getElementById("next").disabled        = true;
        document.getElementById("last").disabled        = true;
        document.getElementById("meta").innerHTML       = "<h1>Coming soon...</h1>";
        document.getElementById("view").innerHTML       = "<h1>Coming soon...</h1>";
        return;
    }

    var episode = series["episodes"][index];
    document.getElementById("title").innerHTML      = "<h1>" + series["meta"]["title"] + "</h1>";
    document.getElementById("first").disabled       = false;
    document.getElementById("previous").disabled    = (index <= 1);
    document.getElementById("about").disabled       = false;
    document.getElementById("next").disabled        = index >= (length - 1);
    document.getElementById("last").disabled        = false;
    
    document.getElementById("meta").innerHTML       = "<h1>" + episode["story"] + " #" + episode["part"] + "</h1>";
    document.getElementById("view").innerHTML       = "<p>"  + episode["notes"] + "</p><img width=\"100%\" src=\"" + name + "_" + episode["number"] + ".jpg\">";
}

/* last
 * @brief   update when first button pressed
 */
function updateToFirst()
{
    if(!(null === series))
    {
        index   = 1;
    }
    update();
}

/* last
 * @brief   update when prev button pressed
 */
function updateToPrevious()
{
    if(!(null === series) && (index > 1))
    {
        index   = index - 1;
    }
    update();
}

/* last
 * @brief   update when about button pressed
 */
function updateToAbout()
{
//                 update();
    document.getElementById("meta").innerHTML       = series["meta"]["about"];
}

/* last
 * @brief   update when next button pressed
 */
function updateToNext()
{
    if(!(null === series) && (index < (length - 1)))
    {
        index   = index + 1;
    }
    update();
}


/* last
 * @brief   update when kast button pressed
 */
function updateToLast()
{
    if(!(null === series))
    {
        index   = length - 1;
    }
    update();
}

/* last
 * @brief   Get series data from the server, update global variables, and update()
 */
function getData()
{
    var file    = name + ".json";
    var xhttp   = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
        series  = JSON.parse(this.responseText);

        // TODO: Error checking
        length  = series["episodes"].length;
        index   = length - 1;
        
        update();
        }
    };
    xhttp.open("GET", file, true);
    xhttp.send();
}
