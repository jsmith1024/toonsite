function getAbout(series)
{
    getEpisode(series, -1);
//     var result  = "All about it."
//     var xhttp   = new XMLHttpRequest();
//     xhttp.onreadystatechange = function()
//     {
//          alert(this.status)
//         if (this.readyState == 4 && this.status == 200)
//         {
//         document.getElementById("view").innerHTML = this.responseText;
//         }
//     };
//     xhttp.open("GET", "about.txt", true);
//     xhttp.send();
//     return(result);
}

// constructor(series)
// {
//     document.write("\nHello");
//     this.series     = series;
//     this.episodes   = [1,2,3];
//     this.i          = this.episodes.length - 1;
// }

// getSeries()
// {
//     var result          = this.series;
//     return(result);
// //  document.write(this.series);
// }

function getEpisode(series, i)
{
    i++;
    var xhttp   = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
//         alert(this.status)
        if (this.readyState == 4 && this.status == 200)
        {
        document.getElementById("view").innerHTML = this.responseText;
        }
    };
//     alert(series + "_" + i.toString() + ".txt");
    var episode     = series + "_" + i.toString() + ".txt"
    alert(episode)
    xhttp.open("GET", episode, true);
    xhttp.send();
//     return(i);
}

function first(series, i)
{
    i               = 0;
    getEpisode(series, i);
    return(i);
}

function previous(series, i)
{
    i --;
    return(i);
}

function next(series, i)
{
    i ++;
    return(i);
}

function last(series, i)
{
    i           = episodes.length - 1;
    return(i);
}
