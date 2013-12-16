// Adapted from rasterize.js, available at
// https://github.com/ariya/phantomjs/blob/master/examples/rasterize.js

var page = require('webpage').create()
var system = require('system')
var address = system.args[1];
var output = system.args[2];
page.viewportSize = { width: 1280, height: 702 }; // Default on my 13" MacBook

page.open(address, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit();
    } else {
        window.setTimeout(function () {
            page.render(output);
            phantom.exit();
        }, 200);
    }
});
