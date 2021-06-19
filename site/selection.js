function getAbout(series)
{
    var file    = "about.txt";
    getEpisode(file);
}

function getEpisode(file)
{
    var xhttp   = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
//         alert(this.status)
        if (this.readyState == 4 && this.status == 200)
        {
        document.getElementById("view").innerHTML = this.responseText;
        }
    };
//     alert(file)
    xhttp.open("GET", file, true);
    xhttp.send();
//     return(i);
}

function first(series, i)
{
    i               = 0;
    num             = i + 1;
    var file        = series[0] + "_" + num.toString() + ".txt"
    getEpisode(file);
    return(i);
}

function previous(series, i)
{
    if(i > 0)
    {
        i --;
        num         = i + 1;
        var file    = series[0] + "_" + num.toString() + ".txt"
        getEpisode(file);
    }
    return(i);
}

function next(series, i)
{
    if(i < series.length - 2)
    {
        i ++;
        num         = i + 1;
        var file    = series[0] + "_" + num.toString() + ".txt"
        getEpisode(file);
    }
    return(i);
}

function last(series, i)
{
    i               = series.length - 2;
    num             = i + 1;
    var file        = series[0] + "_" + num.toString() + ".txt"
    getEpisode(file);
    return(i);
}
