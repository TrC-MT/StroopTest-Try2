#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on June 26, 2023, at 16:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'StroopTestButtons1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'Age': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ttree\\OneDrive\\Old_Pre7-30-2022_Files\\Documents\\PsychopyTests\\Stroop1\\Buttons\\StroopTestButtons1_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True)
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions" ---
instructions = visual.TextStim(win=win, name='instructions',
    text='Click the button for the color of the given word, NOT for the word itself.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_start = visual.ButtonStim(win, 
    text='START', font='Arvo',
    pos=(0, -.5),
    letterHeight=0.05,
    size=(0.5, 0.5), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_start',
    depth=-1
)
button_start.buttonClock = core.Clock()

# --- Initialize components for Routine "trial" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_red = visual.ButtonStim(win, 
    text='Red', font='Arvo',
    pos=(-.8, -.5),
    letterHeight=None,
    size=(0.2, 0.2), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_red',
    depth=-1
)
button_red.buttonClock = core.Clock()
button_blue = visual.ButtonStim(win, 
    text='Blue', font='Arvo',
    pos=(-.4, -.5),
    letterHeight=None,
    size=(0.2, 0.2), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_blue',
    depth=-2
)
button_blue.buttonClock = core.Clock()
button_green = visual.ButtonStim(win, 
    text='Green', font='Arvo',
    pos=(0, -.5),
    letterHeight=None,
    size=(0.2, 0.2), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_green',
    depth=-3
)
button_green.buttonClock = core.Clock()
button_yellow = visual.ButtonStim(win, 
    text='Yellow', font='Arvo',
    pos=(.4, -.5),
    letterHeight=None,
    size=(0.2, 0.2), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_yellow',
    depth=-4
)
button_yellow.buttonClock = core.Clock()
button_purple = visual.ButtonStim(win, 
    text='Purple', font='Arvo',
    pos=(.8, -.5),
    letterHeight=None,
    size=(0.2, 0.2), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_purple',
    depth=-5
)
button_purple.buttonClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
# update component parameters for each repeat
# reset button_start to account for continued clicks & clear times on/off
button_start.reset()
# keep track of which components have finished
InstructionsComponents = [instructions, button_start]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    
    # if instructions is starting this frame...
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions.started')
        # update status
        instructions.status = STARTED
        instructions.setAutoDraw(True)
    
    # if instructions is active this frame...
    if instructions.status == STARTED:
        # update params
        pass
    # *button_start* updates
    
    # if button_start is starting this frame...
    if button_start.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_start.frameNStart = frameN  # exact frame index
        button_start.tStart = t  # local t and not account for scr refresh
        button_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_start, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'button_start.started')
        # update status
        button_start.status = STARTED
        button_start.setAutoDraw(True)
    
    # if button_start is active this frame...
    if button_start.status == STARTED:
        # update params
        pass
        # check whether button_start has been pressed
        if button_start.isClicked:
            if not button_start.wasClicked:
                # if this is a new click, store time of first click and clicked until
                button_start.timesOn.append(button_start.buttonClock.getTime())
                button_start.timesOff.append(button_start.buttonClock.getTime())
            elif len(button_start.timesOff):
                # if click is continuing from last frame, update time of clicked until
                button_start.timesOff[-1] = button_start.buttonClock.getTime()
            if not button_start.wasClicked:
                # end routine when button_start is clicked
                continueRoutine = False
            if not button_start.wasClicked:
                # run callback code when button_start is clicked
                pass
    # take note of whether button_start was clicked, so that next frame we know if clicks are new
    button_start.wasClicked = button_start.isClicked and button_start.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_start.numClicks', button_start.numClicks)
if button_start.numClicks:
   thisExp.addData('button_start.timesOn', button_start.timesOn)
   thisExp.addData('button_start.timesOff', button_start.timesOff)
else:
   thisExp.addData('button_start.timesOn', "")
   thisExp.addData('button_start.timesOff', "")
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StroopTestStimuliButtons1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    text.setColor(Color, colorSpace='rgb')
    text.setText(Word)
    # reset button_red to account for continued clicks & clear times on/off
    button_red.reset()
    # reset button_blue to account for continued clicks & clear times on/off
    button_blue.reset()
    # reset button_green to account for continued clicks & clear times on/off
    button_green.reset()
    # reset button_yellow to account for continued clicks & clear times on/off
    button_yellow.reset()
    # reset button_purple to account for continued clicks & clear times on/off
    button_purple.reset()
    # keep track of which components have finished
    trialComponents = [text, button_red, button_blue, button_green, button_yellow, button_purple]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        # *button_red* updates
        
        # if button_red is starting this frame...
        if button_red.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_red.frameNStart = frameN  # exact frame index
            button_red.tStart = t  # local t and not account for scr refresh
            button_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_red, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_red.started')
            # update status
            button_red.status = STARTED
            button_red.setAutoDraw(True)
        
        # if button_red is active this frame...
        if button_red.status == STARTED:
            # update params
            pass
            # check whether button_red has been pressed
            if button_red.isClicked:
                if not button_red.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_red.timesOn.append(button_red.buttonClock.getTime())
                    button_red.timesOff.append(button_red.buttonClock.getTime())
                elif len(button_red.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_red.timesOff[-1] = button_red.buttonClock.getTime()
                if not button_red.wasClicked:
                    # end routine when button_red is clicked
                    continueRoutine = False
                if not button_red.wasClicked:
                    # run callback code when button_red is clicked
                    pass
        # take note of whether button_red was clicked, so that next frame we know if clicks are new
        button_red.wasClicked = button_red.isClicked and button_red.status == STARTED
        # *button_blue* updates
        
        # if button_blue is starting this frame...
        if button_blue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_blue.frameNStart = frameN  # exact frame index
            button_blue.tStart = t  # local t and not account for scr refresh
            button_blue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_blue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_blue.started')
            # update status
            button_blue.status = STARTED
            button_blue.setAutoDraw(True)
        
        # if button_blue is active this frame...
        if button_blue.status == STARTED:
            # update params
            pass
            # check whether button_blue has been pressed
            if button_blue.isClicked:
                if not button_blue.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_blue.timesOn.append(button_blue.buttonClock.getTime())
                    button_blue.timesOff.append(button_blue.buttonClock.getTime())
                elif len(button_blue.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_blue.timesOff[-1] = button_blue.buttonClock.getTime()
                if not button_blue.wasClicked:
                    # end routine when button_blue is clicked
                    continueRoutine = False
                if not button_blue.wasClicked:
                    # run callback code when button_blue is clicked
                    pass
        # take note of whether button_blue was clicked, so that next frame we know if clicks are new
        button_blue.wasClicked = button_blue.isClicked and button_blue.status == STARTED
        # *button_green* updates
        
        # if button_green is starting this frame...
        if button_green.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_green.frameNStart = frameN  # exact frame index
            button_green.tStart = t  # local t and not account for scr refresh
            button_green.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_green, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_green.started')
            # update status
            button_green.status = STARTED
            button_green.setAutoDraw(True)
        
        # if button_green is active this frame...
        if button_green.status == STARTED:
            # update params
            pass
            # check whether button_green has been pressed
            if button_green.isClicked:
                if not button_green.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_green.timesOn.append(button_green.buttonClock.getTime())
                    button_green.timesOff.append(button_green.buttonClock.getTime())
                elif len(button_green.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_green.timesOff[-1] = button_green.buttonClock.getTime()
                if not button_green.wasClicked:
                    # end routine when button_green is clicked
                    continueRoutine = False
                if not button_green.wasClicked:
                    # run callback code when button_green is clicked
                    pass
        # take note of whether button_green was clicked, so that next frame we know if clicks are new
        button_green.wasClicked = button_green.isClicked and button_green.status == STARTED
        # *button_yellow* updates
        
        # if button_yellow is starting this frame...
        if button_yellow.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_yellow.frameNStart = frameN  # exact frame index
            button_yellow.tStart = t  # local t and not account for scr refresh
            button_yellow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_yellow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_yellow.started')
            # update status
            button_yellow.status = STARTED
            button_yellow.setAutoDraw(True)
        
        # if button_yellow is active this frame...
        if button_yellow.status == STARTED:
            # update params
            pass
            # check whether button_yellow has been pressed
            if button_yellow.isClicked:
                if not button_yellow.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_yellow.timesOn.append(button_yellow.buttonClock.getTime())
                    button_yellow.timesOff.append(button_yellow.buttonClock.getTime())
                elif len(button_yellow.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_yellow.timesOff[-1] = button_yellow.buttonClock.getTime()
                if not button_yellow.wasClicked:
                    # end routine when button_yellow is clicked
                    continueRoutine = False
                if not button_yellow.wasClicked:
                    # run callback code when button_yellow is clicked
                    pass
        # take note of whether button_yellow was clicked, so that next frame we know if clicks are new
        button_yellow.wasClicked = button_yellow.isClicked and button_yellow.status == STARTED
        # *button_purple* updates
        
        # if button_purple is starting this frame...
        if button_purple.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_purple.frameNStart = frameN  # exact frame index
            button_purple.tStart = t  # local t and not account for scr refresh
            button_purple.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_purple, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_purple.started')
            # update status
            button_purple.status = STARTED
            button_purple.setAutoDraw(True)
        
        # if button_purple is active this frame...
        if button_purple.status == STARTED:
            # update params
            pass
            # check whether button_purple has been pressed
            if button_purple.isClicked:
                if not button_purple.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_purple.timesOn.append(button_purple.buttonClock.getTime())
                    button_purple.timesOff.append(button_purple.buttonClock.getTime())
                elif len(button_purple.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_purple.timesOff[-1] = button_purple.buttonClock.getTime()
                if not button_purple.wasClicked:
                    # end routine when button_purple is clicked
                    continueRoutine = False
                if not button_purple.wasClicked:
                    # run callback code when button_purple is clicked
                    pass
        # take note of whether button_purple was clicked, so that next frame we know if clicks are new
        button_purple.wasClicked = button_purple.isClicked and button_purple.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('button_red.numClicks', button_red.numClicks)
    if button_red.numClicks:
       trials.addData('button_red.timesOn', button_red.timesOn)
       trials.addData('button_red.timesOff', button_red.timesOff)
    else:
       trials.addData('button_red.timesOn', "")
       trials.addData('button_red.timesOff', "")
    trials.addData('button_blue.numClicks', button_blue.numClicks)
    if button_blue.numClicks:
       trials.addData('button_blue.timesOn', button_blue.timesOn)
       trials.addData('button_blue.timesOff', button_blue.timesOff)
    else:
       trials.addData('button_blue.timesOn', "")
       trials.addData('button_blue.timesOff', "")
    trials.addData('button_green.numClicks', button_green.numClicks)
    if button_green.numClicks:
       trials.addData('button_green.timesOn', button_green.timesOn)
       trials.addData('button_green.timesOff', button_green.timesOff)
    else:
       trials.addData('button_green.timesOn', "")
       trials.addData('button_green.timesOff', "")
    trials.addData('button_yellow.numClicks', button_yellow.numClicks)
    if button_yellow.numClicks:
       trials.addData('button_yellow.timesOn', button_yellow.timesOn)
       trials.addData('button_yellow.timesOff', button_yellow.timesOff)
    else:
       trials.addData('button_yellow.timesOn', "")
       trials.addData('button_yellow.timesOff', "")
    trials.addData('button_purple.numClicks', button_purple.numClicks)
    if button_purple.numClicks:
       trials.addData('button_purple.timesOn', button_purple.timesOn)
       trials.addData('button_purple.timesOff', button_purple.timesOff)
    else:
       trials.addData('button_purple.timesOn', "")
       trials.addData('button_purple.timesOff', "")
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
