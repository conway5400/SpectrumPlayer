console.log("You are connected!")

var url = "https://dash.edgesuite.net/envivio/Envivio-dash2/manifest.mpd";
var element = document.querySelector("#player")
var player = dashjs.MediaPlayer().create();
var checkForUpdates = true;
player.initialize(element, url, false);


$('#play').on('click', function() {
    player.play();
    checkUpdates();
});

$('#pause').on('click', function() {
    player.pause();
});

function checkUpdates() {
    if(checkForUpdates) {
        console.log('checking for updates')

        try {
                $.get( "/updates", function( command ) {
                    console.log(command)
                    if(command == 'play') {
                        player.play();
                    } else if (command == 'pause') {
                        player.pause();
                    }
                    $('#connectionStatus').html('Connected!');
                    setTimeout(checkUpdates, 1000)
                });
            } catch (error) {
                checkForUpdates = false;
                $('#connectionStatus').html('Error connecting!');
                console.error('there was an error! abandoning ship!')
            }
    }
}

checkUpdates();
