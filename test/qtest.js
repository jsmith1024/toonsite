QUnit.module('control');

QUnit.test( "Test", async assert =>
{
//     getData();
//     var name    = "TEST";
    var series  = null;
//     getData();
//     var length  = 0;
//     var index   = 0;
//     update();   // to a consistent state
//     assert.equal( "TEST",   name );
//     assert.equal( null,     series );
//     getData();  // to use, which will update() when ready
//     assert.equal( index,    0 );
//     let i       = 0;
//     while(i < 1000000000)
//     {
//         i      += 1;
//     }
//     assert.notEqual( null,  series );
//     updateToLast();
//     assert.equal( index,    3 );
//     });
    
    assert.equal( 0,        toon.index );
    toon.last();
    assert.equal( 3,        toon.index );
    toon.first();
    assert.equal( 1,        toon.index );
    toon.next();
    assert.equal( 2,        toon.index );
    toon.previous();
    assert.equal( 1,        toon.index );
    
});

// QUnit.module('updateToFirst', function() {
// //     updateToFirst();
//     QUnit.test('should set i = 1', function(assert) {
//         updateToFirst();
//         assert.equal( i, 1 );
// });
