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
        document.getElementById("about").disabled       = true;
        document.getElementById("title").innerHTML      = "<h1>Coming soon...</h1>";
        document.getElementById("first").disabled       = true;
        document.getElementById("previous").disabled    = true;
        document.getElementById("reload").disabled      = true;
        document.getElementById("next").disabled        = true;
        document.getElementById("last").disabled        = true;
        document.getElementById("meta").innerHTML       = "<h1>Coming soon...</h1>";
        document.getElementById("view").innerHTML       = "<h1>Coming soon...</h1>";
        return;
    }

    var episode = series["episodes"][index];
    document.getElementById("about").disabled       = false;
    document.getElementById("title").innerHTML      = series["meta"]["title"];
    document.getElementById("first").disabled       = false;
    document.getElementById("previous").disabled    = (index <= 1);
    document.getElementById("reload").disabled      = false;
    document.getElementById("next").disabled        = index >= (length - 1);
    document.getElementById("last").disabled        = false;
    
    let data                                        = "Episode #" + episode["number"];
    data                                           += "<h1>" + episode["story"] + " - Part" + episode["part"] + "</h1>";
    document.getElementById("meta").innerHTML       = data;
    
    data                                            = "<img src=\"" + name + "/episodes/" + name + "_" + episode["number"] + ".jpg\">";
    data                                           += "<p>" + episode["notes"] + "</p>";
//     alert(data);
    document.getElementById("view").innerHTML       = data;
}

/* updateToAbout
 * @brief   update when about button pressed
 */
function updateToAbout()
{
    document.getElementById("meta").innerHTML       = series["meta"]["title"];
    document.getElementById("view").innerHTML       = series["meta"]["about"];
}

/* updateToFirst
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

/* updateToPrevious
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

/* reload
 * @brief   update when about button pressed
 */
function reload()
{
    update();
}

/* updateToNext
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


/* updateToLast
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

/* getData
 * @brief   Get series data from the server, update global variables, and update()
 */
function getData()
{
    var file    = name + "/" + name + ".json";
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
