$(function() {
    console.log( "cooking helpers page ready!" );
    stopRecipe();
});

//function to intialize the video player to a given url and set needed event listeners
function intializeVideoPlayer(url) {
    player.initialize(element, url, true);
    player.getDebug().setLogToBrowserConsole(false);
    player.on(dashjs.MediaPlayer.events['PLAYBACK_TIME_UPDATED'],timeUpdated);
}

//function starts recipe
function startRecipe() {

    //hide and show appropriate buttons and items
    $('#startRecipe').css('display', 'none');
    $('#stopRecipe').css('display', 'block');
    $('#pauseRecipe').css('display', 'block');
    $('#resumeRecipe').css('display', 'none');
    $('#nextStep').css('display', 'block');
    $('#restartStep').css('display', 'block');
    $('#previousStep').css('display', 'block');
    $('#progressBar').css('display', 'block');
    $('#recipeName').css('display', 'block');
    $('#currentStepNumber').html(currentStep);
    $('#lastStepNumber').html(steps.length);

    //trigger next step
    nextStep();
}

//function stops recipe and resets variables
function stopRecipe() {

    //hide and show appropriate buttons and items
    $('#startRecipe').css('display', 'block');
    $('#stopRecipe').css('display', 'none');
    $('#pauseRecipe').css('display', 'none');
    $('#resumeRecipe').css('display', 'none');
    $('#nextStep').css('display', 'none');
    $('#restartStep').css('display', 'none');
    $('#previousStep').css('display', 'none');
    $('#progressBar').css('display', 'none');
    $('#recipeName').css('display', 'none');

    if(recipeStarted == true) {
        recipeStarted = false;
        pauseRecipe();
        player.seek(0);
    }

    recipeStarted = false;
    currentStep = 1;
    clearSteps();

}

function pauseRecipe() {
    player.pause();
    $('#pauseRecipe').css('display', 'none');
    if(recipeStarted) {
        $('#resumeRecipe').css('display', 'block');
    }
}

function resumeRecipe() {

    console.log("Checking to see if we need to move on to the next step or not....")

    if(endOfStep) {
        console.log("Looks like we're ready to go to to the next step....")
        nextStep();
    } else {
        player.play();
    }

    $('#pauseRecipe').css('display', 'block');
    $('#resumeRecipe').css('display', 'none');

}

//function tht runs on video event listener change
function timeUpdated(e) {

    //first we get the new time from the player
    var time = Math.floor(e.time);

    //since this event fires multiple times per second
    // we check to ensure the 'second' has actually changed from previous point
    if(time !== currentTime) {
        console.log("Time is different! " + time)

        if(steps[currentStep]) {
            //check to see if this time stamp is the end of a step or not...
            console.log("Next step begins at " + steps[currentStep].fields.startTime);
            if(time == steps[currentStep].fields.startTime) {
                console.warn("End of step....")
                endOfStep = true;
            }
        }

        //when in preview mode, we will ignore all pause points and annotations
        //we will still update the progress at the bottom
        if(previewMode == false) {

            //check to see if this time stamp has any actions or now....
            if(actions[time]) {

                //go through each action for this timestamp
                actions[time].forEach(function(action) {
                    if(action.action == 'pause') {
                        console.warn("I might need to pause here...")
                        console.warn("Checking video skip value...." + videoSkip);

                        //ensure the video hasn't been skipped to intentionally
                        //this is used to avoid pause points conflict when jumping to steps
                        if(videoSkip == false) {
                            console.warn("I'm trying to pause...")
                            pauseRecipe();
                        } else {
                            console.warn("Just kidding, that was a user skip so I won't pause...")
                            // player.play();
                            videoSkip = false;
                            console.warn(videoSkip); 
                        }
                    } else if(action.action == 'timer') {
                        newTimer(action.content);
                        console.log("new timer!")

                    } else if(action.action == 'tip') {
                        newTip(action.content);
                        console.log("new tip!");
                    }
                });
            }
            //updated the current time to the new time
            currentTime = time;

        } else {

            if(recipeStarted == false) {
                player.pause();
            }

            console.log("checking to see if at end of step...")
            if(endOfStep == true) {
                console.warn("end of step!")
                currentStep++;
                updateSteps(currentStep);
                endOfStep = false;
            }
        }

        currentTime = time;
    } 
}

//go to previous step
function previousStep() {

    console.log("Trying to go to the previous step....")
    console.log("My target step is...." + (currentStep - 1));

    //ensure that the target step is not out of bounds
    if(currentStep - 1 < 1) {
       console.error("Oh no! Target step is out of bounds. Ignoring user command!");
       return;
    }

    if(recipeStarted == false) {
        console.log("Recipe hasn't started yet....");
        console.log("Trying to start the recipe!....");
        updateSteps(currentStep);
        player.play();
        recipeStarted = true;
    } else {
        console.log("Recipe has started! Going to the next step...");
        currentStep--;
        updateSteps(currentStep);
        videoSkip = true;
        player.seek(steps[currentStep - 1].fields.startTime);
        player.play();
    } 
}

//restarting the current step
function restartStep() {
    console.log("Attempting to restart step....")
    if(recipeStarted == true) {
        console.log("Recipe in progress, should be able to restart step....")
        videoSkip = true;
        player.seek(steps[currentStep - 1].fields.startTime);
    } else {
        console.error("Recipe not progress, can't restart step....")
    }
}
//go to next step
function nextStep() {

    console.log("Trying to go to the next step....")
    console.log("My target step is...." + (currentStep + 1));

    //ensure that the target step is not out of bounds
    if(currentStep + 1 > steps.length) {
       console.error("Oh no! Target step is out of bounds. Ignoring user command!" + steps.length);
       return;
    }

    if(recipeStarted == false) {
        console.log("Recipe hasn't started....");
        updateSteps(1);
        player.play();
        recipeStarted = true;
    } else {
        console.log("Recipe has started! Going to the next step...");
        currentStep++;
        updateSteps(currentStep);
        // videoSkip = true;
        player.seek(steps[currentStep - 1].fields.startTime);

        if(player.isPaused()) {
            endOfStep = false;
            resumeRecipe();
        } else {
            videoSkip = true;
        }
    }
}

//helper function to set text on step elements
function setText(text, target) {
    if(target == 'previousStep') {
        $('.previousStep h3').html(text)
    } else if (target == 'currentStep') {
        $('.currentStep h3').html(text)
    } else if (target == 'nextStep') {
        $('.nextStep h3').html(text)
    }
}

//clear all steps display
function clearSteps() {
    setText('', 'previousStep');
    setText('', 'currentStep');
    setText('', 'nextStep');
}

//update all steps displays to appropriate values
function updateSteps(targetStep) {
    console.warn("Attempting to updated steps to step #" + targetStep);

    //check for out of bounds first
    //shouldn't hit ever because of checks on next/previous steps
    if(targetStep < 0 || targetStep > steps.length) {
       console.error("Target step is out of bounds! This tutorial has " + steps.length + "steps. Ignoring request...");
       return;
    }

    //handle "previous step display" if at beginning of recipe
    if(targetStep == 1) {
        setText('No previous steps', 'previousStep')
    } else {
        setText(steps[targetStep - 1 - 1].fields.shortDesc, 'previousStep')
    }

    //set current step display
    setText(steps[targetStep - 1].fields.longDesc, 'currentStep');

    //handle "next step display" if at end of recipe
    if(targetStep == steps.length) {
        setText('Enjoy your meal!', 'nextStep')
    } else if(targetStep > steps.length) {
        // setText(steps[targetStep + 1 - 1].fields.shortDesc, 'nextStep')
    } else {
        // $('#currentStepNumber').html(targetStep);
        setText(steps[targetStep + 1 - 1].fields.shortDesc, 'nextStep')
    }

    $('#currentStepNumber').html(targetStep);
}


function newTimer(length, name) {
    var newTimerHtml = '<div class="timer"><h4>Timer</h4><p>' + length + ' seconds</p></div>';
    $(newTimerHtml).insertAfter( ".activityCards h2" );
}

function newTip(tip) {
    var newTipHtml = '<div class="tip"><h4>Tip</h4><p>' + tip + '</p></div>';
    $(newTipHtml).insertAfter( ".activityCards h2" );
}

function newIngredient(id, name, descr) {
    var newIngredientHtml = '<div class="ingredient"><h4>' + name + '</h4><p>(' + descr + ')</p></div>';
    $(newIngredientHtml).insertAfter( ".ingredients h2" );
}
