QUnit.module('control');

QUnit.test( "Test", async assert =>
{
//     getData();
    var name    = "TEST";
    var series  = null;
    var length  = 0;
    var index   = 3;
//     update();   // to a consistent state
    getData();  // to use, which will update() when ready
    assert.equal( index, 3 );
    let i       = 0;
    while(i < 1000000000)
    {
        i      += 1;
    }
    assert.notEqual( null, series );
    updateToFirst();
    assert.equal( index, 1 );
//     });
});

// QUnit.module('updateToFirst', function() {
// //     updateToFirst();
//     QUnit.test('should set i = 1', function(assert) {
//         updateToFirst();
//         assert.equal( i, 1 );
// });
