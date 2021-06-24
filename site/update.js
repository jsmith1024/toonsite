// toonsite

// A javascript package to facilitate a comic strip
// presentation website.

// made by j.smith and j. smith

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

            // First button pressed
            function updateToFirst()
            {
                if(!(null === series))
                {
                    index   = 1;
                }
                update();
            }

            // Previous button pressed
            function updateToPrevious()
            {
                if(!(null === series) && (index > 1))
                {
                    index   = index - 1;
                }
                update();
            }

            // About button pressed
            function updateToAbout()
            {
//                 update();
                document.getElementById("meta").innerHTML       = series["meta"]["about"];
            }

            // Next button pressed
            function updateToNext()
            {
                if(!(null === series) && (index < (length - 1)))
                {
                    index   = index + 1;
                }
                update();
            }

            // Last button pressed
            function updateToLast()
            {
                if(!(null === series))
                {
                    index   = length - 1;
                }
                update();
            }

            // Get series data from the server, update global variables, and update()
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

// /* getSeries
//  * @brief   read in series data
//  * @param   name        (string)    name of series
//  * @param   onReceived  (callback)  name of series
//  */
// function getSeries(name, onReceived)
// {
//     //
//     var file        = name + ".json";
//     alert("Trying to load: " + file);
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function()
//     {
// //         alert(this.status);
//         if (this.readyState == 4 && this.status == 200)
//         {
// //         alert(this.responseText);
//         var series  = JSON.parse(this.responseText);
//         alert(series["meta"]["title"] + " " + series["episodes"][3]["number"].toString()); // If correct, produces "TEST 003"
//         onReceived(series);
//         }
//     };
//     xhttp.open("GET", file, true);
//     xhttp.send();
// }
// 
// /* getEpisode
//  * @brief   display episode material in div "view"
//  * @param   file        (string)    name of file
//  */
// function getEpisode(file)
// {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function()
//     {
//         if (this.readyState == 4 && this.status == 200)
//         {
//             document.getElementById("view").innerHTML = this.responseText + '</p><img width="100%" src="' + file + '.jpg"></img>';
//         }
//     };
//     xhttp.open("GET", file + ".txt", true);
//     xhttp.send();
// }
// 
// /* getEpisodeMeta
//  * @brief   read in series data
//  * @param   episode     (dictionary)    episode data
//  * @return  (dictionary)
//  */
// function getEpisodeMeta(episode)
// {
//     var result      = "</p> Episode: " + episode["number"].toString() + " <h1>" + episode["story"] + "</h1> Part: " + episode["part"] + "</p>";
//     document.getElementById("meta").innerHTML = result;
// }
// 
// /* getAbout
//  * @brief   read in series data
//  * @param   series      (dictionary)    series data
//  */
// function getAbout(series)
// {
//     document.getElementById("meta").innerHTML = series["meta"]["about"];
// }
// 
// /* first
//  * @brief   move to first episode
//  * @param   series      (dictionary)    series data
//  * @return  (integer)
//  */
// function first(series)
// {
//     i               = 0;
//     num             = i + 1;
//     var file        = series["meta"]["title"] + "_" + num.toString();
//     getEpisode(file);
//     getEpisodeMeta(series["episodes"][num]);
//     return(i);
// }
// 
// /* previous
//  * @brief   move to previous episode
//  * @param   series      (dictionary)    series data
//  * @param   i           (integer)       index
//  * @return  (integer)
//  */
// function previous(series, i)
// {
//     if(i > 0)
//     {
//         i --;
//         num         = i + 1;
//         var file    = series["meta"]["title"] + "_" + num.toString();
//         getEpisode(file);
//         getEpisodeMeta(series["episodes"][num]);
//     }
//     return(i);
// }
// 
// /* next
//  * @brief   move to next episode
//  * @param   series      (dictionary)    series data
//  * @param   i           (integer)       index
//  * @return  (integer)
//  */
// function next(series, i)
// {
//     if(i < series["episodes"].length - 1)
//     {
//         i ++;
//         num         = i + 1;
//         var file    = series["meta"]["title"] + "_" + num.toString();
//         getEpisode(file);
//         getEpisodeMeta(series["episodes"][num]);
//     }
//     return(i);
// }
// 
// /* last
//  * @brief   move to last episode
//  * @param   series      (dictionary)    series data
//  * @return  (integer)
//  */
// function last(series)
// {
//     i               = series["episodes"].length - 2;
//     num             = i + 1;
//     var file        = series["meta"]["title"] + "_" + num.toString();
//     getEpisode(file);
//     getEpisodeMeta(series["episodes"][num]);
//     return(i);
// }
