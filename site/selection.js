// toonsite

// A javascript package to facilitate a comic strip
// presentation website.



function getSeries(name, callback)
{
//     alert("trying to import json...");
//     
//     var xobj = new XMLHttpRequest();
//         xobj.overrideMimeType("application/json");
//     xobj.open('GET', name  + '.json', true); // Replace 'my_data' with the path to your file
//     xobj.onreadystatechange = function () {
//         if (xobj.readyState == 4 && xobj.status == "200") {
//             alert(xobj.responseText);
//             callback(xobj.responseText);
// //             return(JSON.parse(xobj.responseText);
//         }
//     };
//     alert(xobj.responseText);
//     xobj.send(null);
    
// //     return(JSON.parse(xobj.responseText));
    
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
}

function getEpisodeMeta(episode)
{
    var result      = "</p> Episode: " + episode["number"].toString() + " <h1>" + episode["story"] + "</h1> Part: " + episode["part"] + "</p>";
//     alert(result);
    document.getElementById("meta").innerHTML = result;
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
    getEpisodeMeta(series["episodes"][num]);
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
        getEpisodeMeta(series["episodes"][num]);
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
        getEpisodeMeta(series["episodes"][num]);
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
    getEpisodeMeta(series["episodes"][num]);
    return(i);
}
