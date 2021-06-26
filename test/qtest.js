QUnit.module('control');

QUnit.test( "Test", async assert =>
{
    getData();
    var name    = "TEST";
    var series  = null;
    var length  = 0;
    var index   = 3;
    update();   // to a consistent state
    getData();  // to use, which will update() when ready
//     let i       = 0;
//     while(i < 10000000)
//     {
//         i      += 1;
//     }
    assert.equal( index, 3 );
    updateToFirst();
//     i           = 0;
//     while(i < 10000000)
//     {
//         i      += 1;
//     }
    assert.equal( iindex, 1 );
//     QUnit.module('control', assert.equal( i, 3 ))
//     QUnit.test('should add two numbers', function(assert) {
//       assert.equal(add(1, 1), 2);
//     });
//     QUnit.module('add', function() {
//     QUnit.test('should add two numbers', function(assert) {
//       assert.equal(add(1, 1), 2);
//     });
});

// QUnit.module('updateToFirst', function() {
// //     updateToFirst();
//     QUnit.test('should set i = 1', function(assert) {
//         updateToFirst();
//         assert.equal( i, 1 );
// });
