/*************************** 
 * Strooptestbuttons1 Test *
 ***************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'StroopTestButtons1';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
    'Age': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'StroopTestStimuliButtons1.xlsx', 'path': 'StroopTestStimuliButtons1.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var instructions;
var button_start;
var trialClock;
var text;
var button_red;
var button_blue;
var button_green;
var button_yellow;
var button_purple;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: 'Click the button for the color of the given word, NOT for the word itself.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  button_start = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_start',
    text: 'START',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.5)],
    letterHeight: 0.05,
    size: [0.5, 0.5],
    depth: -1
  });
  button_start.clock = new util.Clock();
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  button_red = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_red',
    text: 'Red',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.8), (- 0.5)],
    letterHeight: null,
    size: [0.2, 0.2],
    depth: -1
  });
  button_red.clock = new util.Clock();
  
  button_blue = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_blue',
    text: 'Blue',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.4), (- 0.5)],
    letterHeight: null,
    size: [0.2, 0.2],
    depth: -2
  });
  button_blue.clock = new util.Clock();
  
  button_green = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_green',
    text: 'Green',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.5)],
    letterHeight: null,
    size: [0.2, 0.2],
    depth: -3
  });
  button_green.clock = new util.Clock();
  
  button_yellow = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_yellow',
    text: 'Yellow',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.4, (- 0.5)],
    letterHeight: null,
    size: [0.2, 0.2],
    depth: -4
  });
  button_yellow.clock = new util.Clock();
  
  button_purple = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_purple',
    text: 'Purple',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.8, (- 0.5)],
    letterHeight: null,
    size: [0.2, 0.2],
    depth: -5
  });
  button_purple.clock = new util.Clock();
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // reset button_start to account for continued clicks & clear times on/off
    button_start.reset()
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instructions);
    InstructionsComponents.push(button_start);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions* updates
    if (t >= 0.0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }

    
    // *button_start* updates
    if (t >= 0 && button_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_start.tStart = t;  // (not accounting for frame time here)
      button_start.frameNStart = frameN;  // exact frame index
      
      button_start.setAutoDraw(true);
    }

    if (button_start.status === PsychoJS.Status.STARTED) {
      // check whether button_start has been pressed
      if (button_start.isClicked) {
        if (!button_start.wasClicked) {
          // store time of first click
          button_start.timesOn.push(button_start.clock.getTime());
          button_start.numClicks += 1;
          // store time clicked until
          button_start.timesOff.push(button_start.clock.getTime());
        } else {
          // update time clicked until;
          button_start.timesOff[button_start.timesOff.length - 1] = button_start.clock.getTime();
        }
        if (!button_start.wasClicked) {
          // end routine when button_start is clicked
          continueRoutine = false;
        }
        // if button_start is still clicked next frame, it is not a new click
        button_start.wasClicked = true;
      } else {
        // if button_start is clicked next frame, it is a new click
        button_start.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_start hasn't started / has finished
      button_start.clock.reset();
      // if button_start is clicked next frame, it is a new click
      button_start.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('button_start.numClicks', button_start.numClicks);
    psychoJS.experiment.addData('button_start.timesOn', button_start.timesOn);
    psychoJS.experiment.addData('button_start.timesOff', button_start.timesOff);
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'StroopTestStimuliButtons1.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text.setColor(new util.Color(Color));
    text.setText(Word);
    // reset button_red to account for continued clicks & clear times on/off
    button_red.reset()
    // reset button_blue to account for continued clicks & clear times on/off
    button_blue.reset()
    // reset button_green to account for continued clicks & clear times on/off
    button_green.reset()
    // reset button_yellow to account for continued clicks & clear times on/off
    button_yellow.reset()
    // reset button_purple to account for continued clicks & clear times on/off
    button_purple.reset()
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(text);
    trialComponents.push(button_red);
    trialComponents.push(button_blue);
    trialComponents.push(button_green);
    trialComponents.push(button_yellow);
    trialComponents.push(button_purple);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *button_red* updates
    if (t >= 0 && button_red.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_red.tStart = t;  // (not accounting for frame time here)
      button_red.frameNStart = frameN;  // exact frame index
      
      button_red.setAutoDraw(true);
    }

    if (button_red.status === PsychoJS.Status.STARTED) {
      // check whether button_red has been pressed
      if (button_red.isClicked) {
        if (!button_red.wasClicked) {
          // store time of first click
          button_red.timesOn.push(button_red.clock.getTime());
          button_red.numClicks += 1;
          // store time clicked until
          button_red.timesOff.push(button_red.clock.getTime());
        } else {
          // update time clicked until;
          button_red.timesOff[button_red.timesOff.length - 1] = button_red.clock.getTime();
        }
        if (!button_red.wasClicked) {
          // end routine when button_red is clicked
          continueRoutine = false;
        }
        // if button_red is still clicked next frame, it is not a new click
        button_red.wasClicked = true;
      } else {
        // if button_red is clicked next frame, it is a new click
        button_red.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_red hasn't started / has finished
      button_red.clock.reset();
      // if button_red is clicked next frame, it is a new click
      button_red.wasClicked = false;
    }
    
    // *button_blue* updates
    if (t >= 0 && button_blue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_blue.tStart = t;  // (not accounting for frame time here)
      button_blue.frameNStart = frameN;  // exact frame index
      
      button_blue.setAutoDraw(true);
    }

    if (button_blue.status === PsychoJS.Status.STARTED) {
      // check whether button_blue has been pressed
      if (button_blue.isClicked) {
        if (!button_blue.wasClicked) {
          // store time of first click
          button_blue.timesOn.push(button_blue.clock.getTime());
          button_blue.numClicks += 1;
          // store time clicked until
          button_blue.timesOff.push(button_blue.clock.getTime());
        } else {
          // update time clicked until;
          button_blue.timesOff[button_blue.timesOff.length - 1] = button_blue.clock.getTime();
        }
        if (!button_blue.wasClicked) {
          // end routine when button_blue is clicked
          continueRoutine = false;
        }
        // if button_blue is still clicked next frame, it is not a new click
        button_blue.wasClicked = true;
      } else {
        // if button_blue is clicked next frame, it is a new click
        button_blue.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_blue hasn't started / has finished
      button_blue.clock.reset();
      // if button_blue is clicked next frame, it is a new click
      button_blue.wasClicked = false;
    }
    
    // *button_green* updates
    if (t >= 0 && button_green.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_green.tStart = t;  // (not accounting for frame time here)
      button_green.frameNStart = frameN;  // exact frame index
      
      button_green.setAutoDraw(true);
    }

    if (button_green.status === PsychoJS.Status.STARTED) {
      // check whether button_green has been pressed
      if (button_green.isClicked) {
        if (!button_green.wasClicked) {
          // store time of first click
          button_green.timesOn.push(button_green.clock.getTime());
          button_green.numClicks += 1;
          // store time clicked until
          button_green.timesOff.push(button_green.clock.getTime());
        } else {
          // update time clicked until;
          button_green.timesOff[button_green.timesOff.length - 1] = button_green.clock.getTime();
        }
        if (!button_green.wasClicked) {
          // end routine when button_green is clicked
          continueRoutine = false;
        }
        // if button_green is still clicked next frame, it is not a new click
        button_green.wasClicked = true;
      } else {
        // if button_green is clicked next frame, it is a new click
        button_green.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_green hasn't started / has finished
      button_green.clock.reset();
      // if button_green is clicked next frame, it is a new click
      button_green.wasClicked = false;
    }
    
    // *button_yellow* updates
    if (t >= 0 && button_yellow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_yellow.tStart = t;  // (not accounting for frame time here)
      button_yellow.frameNStart = frameN;  // exact frame index
      
      button_yellow.setAutoDraw(true);
    }

    if (button_yellow.status === PsychoJS.Status.STARTED) {
      // check whether button_yellow has been pressed
      if (button_yellow.isClicked) {
        if (!button_yellow.wasClicked) {
          // store time of first click
          button_yellow.timesOn.push(button_yellow.clock.getTime());
          button_yellow.numClicks += 1;
          // store time clicked until
          button_yellow.timesOff.push(button_yellow.clock.getTime());
        } else {
          // update time clicked until;
          button_yellow.timesOff[button_yellow.timesOff.length - 1] = button_yellow.clock.getTime();
        }
        if (!button_yellow.wasClicked) {
          // end routine when button_yellow is clicked
          continueRoutine = false;
        }
        // if button_yellow is still clicked next frame, it is not a new click
        button_yellow.wasClicked = true;
      } else {
        // if button_yellow is clicked next frame, it is a new click
        button_yellow.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_yellow hasn't started / has finished
      button_yellow.clock.reset();
      // if button_yellow is clicked next frame, it is a new click
      button_yellow.wasClicked = false;
    }
    
    // *button_purple* updates
    if (t >= 0 && button_purple.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_purple.tStart = t;  // (not accounting for frame time here)
      button_purple.frameNStart = frameN;  // exact frame index
      
      button_purple.setAutoDraw(true);
    }

    if (button_purple.status === PsychoJS.Status.STARTED) {
      // check whether button_purple has been pressed
      if (button_purple.isClicked) {
        if (!button_purple.wasClicked) {
          // store time of first click
          button_purple.timesOn.push(button_purple.clock.getTime());
          button_purple.numClicks += 1;
          // store time clicked until
          button_purple.timesOff.push(button_purple.clock.getTime());
        } else {
          // update time clicked until;
          button_purple.timesOff[button_purple.timesOff.length - 1] = button_purple.clock.getTime();
        }
        if (!button_purple.wasClicked) {
          // end routine when button_purple is clicked
          continueRoutine = false;
        }
        // if button_purple is still clicked next frame, it is not a new click
        button_purple.wasClicked = true;
      } else {
        // if button_purple is clicked next frame, it is a new click
        button_purple.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_purple hasn't started / has finished
      button_purple.clock.reset();
      // if button_purple is clicked next frame, it is a new click
      button_purple.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('button_red.numClicks', button_red.numClicks);
    psychoJS.experiment.addData('button_red.timesOn', button_red.timesOn);
    psychoJS.experiment.addData('button_red.timesOff', button_red.timesOff);
    psychoJS.experiment.addData('button_blue.numClicks', button_blue.numClicks);
    psychoJS.experiment.addData('button_blue.timesOn', button_blue.timesOn);
    psychoJS.experiment.addData('button_blue.timesOff', button_blue.timesOff);
    psychoJS.experiment.addData('button_green.numClicks', button_green.numClicks);
    psychoJS.experiment.addData('button_green.timesOn', button_green.timesOn);
    psychoJS.experiment.addData('button_green.timesOff', button_green.timesOff);
    psychoJS.experiment.addData('button_yellow.numClicks', button_yellow.numClicks);
    psychoJS.experiment.addData('button_yellow.timesOn', button_yellow.timesOn);
    psychoJS.experiment.addData('button_yellow.timesOff', button_yellow.timesOff);
    psychoJS.experiment.addData('button_purple.numClicks', button_purple.numClicks);
    psychoJS.experiment.addData('button_purple.timesOn', button_purple.timesOn);
    psychoJS.experiment.addData('button_purple.timesOff', button_purple.timesOff);
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
