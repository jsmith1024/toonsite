QUnit.module('episode');

QUnit.test( "Episode", async assert =>
{
    assert.equal( 0,        episode.index );
    episode.last();
    assert.equal( 3,        episode.index );
    episode.first();
    assert.equal( 1,        episode.index );
    episode.next();
    assert.equal( 2,        episode.index );
    episode.previous();
    assert.equal( 1,        episode.index );
    
});

// QUnit.module('updateToFirst', function() {
// //     updateToFirst();
//     QUnit.test('should set i = 1', function(assert) {
//         updateToFirst();
//         assert.equal( i, 1 );
// });
