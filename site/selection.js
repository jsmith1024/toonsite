function getEpisode(file)
{
    var xhttp   = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
//         alert(this.status)
        if (this.readyState == 4 && this.status == 200)
        {
        document.getElementById("view").innerHTML = this.responseText + '</p><img src="' + file + '.jpg"></img>';
        }
    };
    alert(file);
    xhttp.open("GET", file + ".txt", true);
    xhttp.send();
//     return(i);
}

function getAbout(name, series)
{
    var file    = "about";
    getEpisode(file);
}

function first(name, series, i)
{
    alert("name: " + name);
    i               = 0;
    num             = i + 1;
    var file        = name + "_" + num.toString()
    getEpisode(file);
    return(i);
}

function previous(name, series, i)
{
    if(i > 0)
    {
    alert("name: " + name);
        i --;
        num         = i + 1;
        var file    = name + "_" + num.toString()
        getEpisode(file);
    }
    return(i);
}

function next(name, series, i)
{
    if(i < series.length - 2)
    {
    alert("name: " + name);
        i ++;
        num         = i + 1;
        var file    = name + "_" + num.toString()
        getEpisode(file);
    }
    return(i);
}

function last(name, series, i)
{
    alert("name: " + name);
    i               = series.length - 2;
    num             = i + 1;
    var file        = name + "_" + num.toString()
    getEpisode(file);
    return(i);
}
