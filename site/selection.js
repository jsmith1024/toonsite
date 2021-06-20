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
return({"title": "TEST", "about": "This is a test, only a test.", "Episodes": [{ "number": 001, "story": "the test", "part": 1, "notes": "hello"}, { "number": 002, "story": "the test", "part": 2, "notes": "hello"}, { "number": 003, "story": "the test", "part": 3, "notes": "hello"}] });
}

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
//     alert(file);
    xhttp.open("GET", file + ".txt", true);
    xhttp.send();
//     return(i);
}

function getAbout(series)
{
    document.getElementById("view").innerHTML = series["about"];
}

function first(series, i)
{
    i               = 0;
    num             = i + 1;
//     alert("name: " + series["title"] + num);
    var file        = series["title"] + "_" + num.toString();
    getEpisode(file);
    return(i);
}

function previous(series, i)
{
    if(i > 0)
    {
        i --;
        num         = i + 1;
//         alert("name: " + series["title"] + num);
        var file    = series["title"] + "_" + num.toString();
        getEpisode(file);
    }
    return(i);
}

function next(series, i)
{
    if(i < series["Episodes"].length - 1)
    {
        i ++;
        num         = i + 1;
//         alert("name: " + series["title"] + num);
        var file    = series["title"] + "_" + num.toString();
        getEpisode(file);
    }
    return(i);
}

function last(series, i)
{
    i               = series["Episodes"].length - 1;
    num             = i + 1;
//     alert("name: " + series["title"] + num);
    var file        = series["title"] + "_" + num.toString();
    getEpisode(file);
    return(i);
}
