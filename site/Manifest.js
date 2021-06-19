class Manifest
{
    constructor(series)
    {
        document.write("\nHello");
        this.series     = series;
        this.episodes   = [1,2,3];
        this.i          = this.episodes.length - 1;
    }
    
    getSeries()
    {
        var result          = this.series;
        return(result);
//         document.write(this.series);
    }
    
    getFirst()
    {
        return(0);
    }
    
    getPrevious()
    {
        this.i --;
        return(this.i);
    }
    
    getNext()
    {
        this.i ++;
        return(this.i);
    }
    
    getLast()
    {
        this.i              = this.episodes.length - 1;
        return(this.i);
    }
}
