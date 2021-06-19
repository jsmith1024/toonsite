class Manifest
{
    constructor(series)
    {
        var this.series     = series;
        var this.episodes   = [];
        var this.i          = this.episodes.length - 1;
    }
    
//     toString()
//     {
//         var result          = this.series;
//         return result;
//     }
    
    get previous()
    {
        this.i              = this.i - 1;
        return this.i;
    }
    
    get next()
    {
        this.i              = this.i + 1;
        return this.i;
    }
    get current()
    {
        this.i              = this.episodes.length - 1;
        return this.i;
    }
}
