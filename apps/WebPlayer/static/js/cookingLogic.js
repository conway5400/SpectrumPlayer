//variable declarations

//video player declartions
var element = document.querySelector("#player")
var player = dashjs.MediaPlayer().create();

//data variable declarations for page and json
var tutorialId = null;
var tutorial = null;
var steps = null;
var actions = [[{'action' : 'pause'}]];

//recipe progress trackers and variables
var pausePoints = [0];
var videoSkip = false;
var currentTime = null;
var currentStep = 1;
var recipeStarted = false;
var checkForUpdates = true;
var previewMode = false;
var endOfStep = false;

$(function() {
    console.log( "cooking logic page ready!" ); 
});


//function to pass tutorial id from html to script & load page data from tutorial
function setTutorialId(id) {
    console.log("Setting tutorial id to specified value...")
    stopRecipe();
    tutorialId = id;
    loadPage();
}

//load all page content
function loadPage() {
    console.warn("Attempting to load all page data...")
    //build url to get page info from backend
    var url = "http://spectrumplayer.ngrok.io/api/tutorials/" + tutorialId;
    // var url = "/api/tutorials/" + tutorialId;

    //populate page info from backend and set vaars
    $.get(url, function( data ) {

        // get items from data
        data = JSON.parse(data);
        tutorial = data.tutorial[0].fields
        steps = data.steps;
        var actionsJson = data.actions;

        //load video files
        var videoUrl = tutorial.video;  
        intializeVideoPlayer(videoUrl);

        $('#recipeName').html(tutorial.name);

        //build out action points
        actionsJson.forEach(function(action, index) {
            action = action.fields;

            if(actions[action.timestamp]) {
                actions[action.timestamp].push(action)
            } else {
                actions[action.timestamp] = [action]
            }
        })
       
        console.log(actions);

        console.warn("All page data loaded!")
        checkUpdates();

    }); 

}

//check server for command updates and handle appropriately
function checkUpdates() {
    if(checkForUpdates) {
        try {
            // $.get( "/updates", function( command ) {
            $.get( "http://spectrumplayer.ngrok.io/updates", function( command ) {
                // console.log("Updates: " + command);

                switch(command) {
                    case "StartRecipe":
                        console.log("Starting recipe...")
                        startRecipe();
                        break;

                    case "StopRecipe":
                        console.log("Stopping recipe...")
                        stopRecipe();
                        break;

                    case "NextStep":
                        console.log("Going to next step...")
                        nextStep();
                        break;

                    case "PauseRecipe":
                        console.log("Pausing recipe...")
                        pauseRecipe();
                        break;

                    case "PreviousStep":
                        console.log("Going back a step...")
                        previousStep();
                        break;

                    case "ResumeRecipe":
                        console.log("Resuming recipe...")
                        resumeRecipe();
                        break;

                    case "RestartStep":
                        console.log("Restarting step...")
                        restartStep();
                        break;
                }
                
                setTimeout(checkUpdates, 500)
            });
        } catch (error) {
            checkForUpdates = false;
            console.error('There was an error connecting to server! Abandoning ship!')
        }
    }
}

//button event listeners
$('#nextStep').on('click', nextStep);
$('#restartStep').on('click', restartStep);
$('#previousStep').on('click', previousStep);
$('#startRecipe').on('click', startRecipe);
$('#stopRecipe').on('click', stopRecipe);
$('#pauseRecipe').on('click', pauseRecipe);
$('#resumeRecipe').on('click', resumeRecipe);

$('#viewModeSwitch').change(function(){
    if($(this).is(':checked')) {
        console.warn("preview mode on")
        previewMode = true;
        // Checkbox is checked..
    } else {
        console.warn("preview mode off")
        previewMode = false;
    }
});
