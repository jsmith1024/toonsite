function getSeries(name)
{
//     var xhttp   = new XMLHttpRequest();
//     xhttp.onreadystatechange = function()
//     {
//         alert(this.status)
//         if (this.readyState == 4 && this.status == 200)
//         {
// //         document.getElementById("view").innerHTML = this.responseText + '</p><img src="' + file + '.jpg"></img>';
// //         import series from name + '.json';
//             var data    = callback(this.responseText);
//             alert("data: " + data);
//             var series  = parse(data);
//         }
//     };
//     alert(file);
//     xhttp.open("GET", name + ".json", true);
//     xhttp.send();
//     alert("series: " + series["name"]);
//     document.write("</p>TYPE:&nbsp;&nbsp;" + typeof(series));
//     return(series);
return({"meta": {"title": "TEST", "about": "This is a test, only a test.", "notes": "none"}, "episodes": [{}, { "number": 001, "story": "the test", "part": 1, "notes": "hello"}, { "number": 002, "story": "the test", "part": 2, "notes": "hello"}, { "number": 003, "story": "the test", "part": 3, "notes": "hello"}] });
}

function getEpisode(file)
{
    var xhttp   = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
//         alert(this.status)
        if (this.readyState == 4 && this.status == 200)
        {
            document.getElementById("view").innerHTML = this.responseText + '</p><img width="100%" src="' + file + '.jpg"></img>';
        }
    };
//     alert(file);
    xhttp.open("GET", file + ".txt", true);
    xhttp.send();
//     return(i);
}

function getEpisodeMeta(episode)
{
//     alert("HERE");
//     alert("</p>" + episode["number"]+ " <h1>" + episode["story"] + "</h1> " + episode["part"] + "</p>");
    document.getElementById("meta").innerHTML = "</p>" + episode["number"] + " <h1>" + episode["story"] + "</h1> " + episode["part"] + "</p>");
}

function getAbout(series)
{
    document.getElementById("meta").innerHTML = series["meta"]["about"];
}

function first(series)
{
    i               = 0;
    num             = i + 1;
//     alert("name: " + series["meta"]["title"] + num);
    var file        = series["meta"]["title"] + "_" + num.toString();
    getEpisode(file);
//     getEpisodeMeta(series["episodes"][i]);
    return(i);
}

function previous(series, i)
{
    if(i > 0)
    {
        i --;
        num         = i + 1;
//         alert("name: " + series["meta"]["title"] + num);
        var file    = series["meta"]["title"] + "_" + num.toString();
        getEpisode(file);
//         getEpisodeMeta(series["episodes"][i]);
    }
    return(i);
}

function next(series, i)
{
    if(i < series["episodes"].length - 1)
    {
        i ++;
        num         = i + 1;
//         alert("name: " + series["meta"]["title"] + num);
        var file    = series["meta"]["title"] + "_" + num.toString();
        getEpisode(file);
//         getEpisodeMeta(series["episodes"][i]);
    }
    return(i);
}

function last(series)
{
    i               = series["episodes"].length - 2;
    num             = i + 1;
//     alert("name: " + series["meta"]["title"] + num);
    var file        = series["meta"]["title"] + "_" + num.toString();
    getEpisode(file);
//     getEpisodeMeta(series["episodes"][i]);
    return(i);
}
