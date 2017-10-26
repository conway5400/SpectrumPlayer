console.log("You are connected!")

var url = "http://dash.edgesuite.net/envivio/Envivio-dash2/manifest.mpd";
var element = document.querySelector("#player")
var player = dashjs.MediaPlayer().create();
var checkForUpdates = true;

player.initialize(element, url, true);

$('#play').on('click', function() {
    player.play();
    checkForUpdates = true;
    checkUpdates();
});

$('#pause').on('click', function() {
    player.pause();
});

$('#enableMonitoring').on('click', function() {
    checkForUpdates = true;
});

$('#disableMonitoring').on('click', function() {
    checkForUpdates = false;
});



function checkUpdates() {
    if(checkForUpdates) {
        console.log('checking for updates')
        setTimeout(checkUpdates, 1000);
    }
}
