#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on Tue Mar 17 16:23:19 2026
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'products_online'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant_ID': '',
    'age': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s/%s_%s_%s' % (expInfo['participant_ID'], expInfo['participant_ID'], expName, expInfo['date'].split('_')[0])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/valentinaparada/Documents/experiemnt/products_online_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    text_welcome = visual.TextStim(win=win, name='text_welcome',
        text='Welcome!\nThis is a decision-making experiment\nPress SPACE to start',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions" ---
    text_instructions = visual.TextStim(win=win, name='text_instructions',
        text='INSTRUCTIONS:\nPlease answer these 3 questions:\n- How much do you LIKE the product?\n- How TASTY do you think the product is?\n- How HEALTHY do you think the product is?\n\nRate each question from 0 (not at all) to 7 (very much).\n\nUse the mouse to move the slider and click to confirm your rating.\nYou will have 8 seconds to answer each question.\n\nPress SPACE to begin the experiment',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_instructions = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "setOrder" ---
    
    # --- Initialize components for Routine "fixation" ---
    text_fixation = visual.TextStim(win=win, name='text_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ratingTrial" ---
    # Run 'Begin Experiment' code from ratingCode
    import random
    from psychopy import core
    TIME_LIMIT = 8
    all_questions = [
        ('liking', 'How much do you LIKE the product?'),
        ('taste', 'How TASTY do you think the product is?'),
        ('health', 'How HEALTHY do you think the product is?')
    ]
    questionClock = core.Clock()
    delayClock = core.Clock()
    SLIDER_MIN = 0
    SLIDER_MAX = 7
    SLIDER_WIDTH = 0.72
    productImage = visual.ImageStim(
        win=win,
        name='productImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.14), draggable=False, size=(0.60, 0.60),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    questionText = visual.TextStim(win=win, name='questionText',
        text='placeholder',
        font='Arial',
        pos=(0, -0.22), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ratingValueText = visual.TextStim(win=win, name='ratingValueText',
        text='Rating:',
        font='Arial',
        pos=(0, -0.26), draggable=False, height=0.028, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ratingSlider = visual.Slider(win=win, name='ratingSlider',
        startValue=None, size=(0.7, 0.05), pos=(0, -0.33), units=win.units,
        labels=[0,1,2,3,4,5,6,7], ticks=(0, 1, 2, 3, 4, 5, 6, 7), granularity=0.1,
        style='slider', styleTweaks=[], opacity=None,
        labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
        font='Arial', labelHeight=0.05,
        flip=False, ori=0.0, depth=-4, readOnly=False)
    sliderCover = visual.Rect(
        win=win, name='sliderCover',
        width=(0.80, 0.18)[0], height=(0.80, 0.18)[1],
        ori=0.0, pos=(0, -0.36), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='black', fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    ratingMouse = event.Mouse(win=win)
    x, y = [None, None]
    ratingMouse.mouseClock = core.Clock()
    leftAnchor = visual.TextStim(win=win, name='leftAnchor',
        text='Not at all',
        font='Arial',
        pos=(-0.35, -0.44), draggable=False, height=0.022, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    rightAnchor = visual.TextStim(win=win, name='rightAnchor',
        text='Very much',
        font='Arial',
        pos=(0.35, -0.44), draggable=False, height=0.022, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    warningText = visual.TextStim(win=win, name='warningText',
        text='Please answer before 8 seconds',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "memoryTrial" ---
    # Run 'Begin Experiment' code from memoryCode
    MEMORY_TRIGGERS = {
        'Tapuchips': 1,
        'Nutella': 1,
        'Cheetos': 1,
        'CocaColaZero': 1,
    }
    
    memory_counts = {
        'Tapuchips': 0,
        'Nutella': 0,
        'Cheetos': 0,
        'CocaColaZero': 0,
    }
    memory_target_occurrence = {}
    for prod in ['Tapuchips', 'Nutella', 'Cheetos', 'CocaColaZero']:
        memory_target_occurrence[prod] = random.choice([1, 2, 3])
    all_products = ["Allin", "Cheetos", "ChocolatePara", "CocaColaZero", "Cornflakes", "MangoFree", "Nutella", "Slimdelis", "Tamar", "Tapuchips", "TimTam", "WaffleCrisp", "XL"]
    memoryQuestion = visual.TextStim(win=win, name='memoryQuestion',
        text='Which product was shown in the previous trial?\n\nUse keys 1, 2, or 3 to respond',
        font='Arial',
        pos=(0, 0.20), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    opt1Text = visual.TextStim(win=win, name='opt1Text',
        text='1',
        font='Arial',
        pos=(0, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    opt2Text = visual.TextStim(win=win, name='opt2Text',
        text='2',
        font='Arial',
        pos=(0, -0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    opt3Text = visual.TextStim(win=win, name='opt3Text',
        text='3',
        font='Arial',
        pos=(0, -0.15), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    memoryKey = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "thanks" ---
    endText = visual.TextStim(win=win, name='endText',
        text='Thank you!\nPress SPACE to exit.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endKey = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[text_welcome, key_resp],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
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
    
    # --- Run Routine "Welcome" ---
    thisExp.currentRoutine = Welcome
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_welcome* updates
        
        # if text_welcome is starting this frame...
        if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_welcome.frameNStart = frameN  # exact frame index
            text_welcome.tStart = t  # local t and not account for scr refresh
            text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_welcome.started')
            # update status
            text_welcome.status = STARTED
            text_welcome.setAutoDraw(True)
        
        # if text_welcome is active this frame...
        if text_welcome.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Welcome,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Welcome.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Welcome.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[text_instructions, key_resp_instructions],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_instructions
    key_resp_instructions.keys = []
    key_resp_instructions.rt = []
    _key_resp_instructions_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
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
    
    # --- Run Routine "instructions" ---
    thisExp.currentRoutine = instructions
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instructions* updates
        
        # if text_instructions is starting this frame...
        if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instructions.frameNStart = frameN  # exact frame index
            text_instructions.tStart = t  # local t and not account for scr refresh
            text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_instructions.started')
            # update status
            text_instructions.status = STARTED
            text_instructions.setAutoDraw(True)
        
        # if text_instructions is active this frame...
        if text_instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_instructions* updates
        waitOnFlip = False
        
        # if key_resp_instructions is starting this frame...
        if key_resp_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_instructions.frameNStart = frameN  # exact frame index
            key_resp_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_instructions.started')
            # update status
            key_resp_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_instructions_allKeys):
                key_resp_instructions.keys = _key_resp_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_instructions.rt = _key_resp_instructions_allKeys[-1].rt
                key_resp_instructions.duration = _key_resp_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if key_resp_instructions.keys in ['', [], None]:  # No response was made
        key_resp_instructions.keys = None
    thisExp.addData('key_resp_instructions.keys',key_resp_instructions.keys)
    if key_resp_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_instructions.rt', key_resp_instructions.rt)
        thisExp.addData('key_resp_instructions.duration', key_resp_instructions.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "setOrder" ---
    # create an object to store info about Routine setOrder
    setOrder = data.Routine(
        name='setOrder',
        components=[],
    )
    setOrder.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_serOrder
    all_trials = data.importConditions('image_table.csv')
    row_order = list(range(len(all_trials)))
    def has_adjacent_same_product(order):
    
        for i in range(len(order) - 1):
    
            if all_trials[order[i]]['product_id'] == all_trials[order[i + 1]]['product_id']:
    
                return True
    
        return False
    random.shuffle(row_order)
    while has_adjacent_same_product(row_order):
        random.shuffle(row_order)
    selected_rows_str = ",".join(str(i) for i in row_order)
    continueRoutine = False
    
    
    # store start times for setOrder
    setOrder.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    setOrder.tStart = globalClock.getTime(format='float')
    setOrder.status = STARTED
    thisExp.addData('setOrder.started', setOrder.tStart)
    setOrder.maxDuration = None
    # keep track of which components have finished
    setOrderComponents = setOrder.components
    for thisComponent in setOrder.components:
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
    
    # --- Run Routine "setOrder" ---
    thisExp.currentRoutine = setOrder
    setOrder.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=setOrder,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            setOrder.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if setOrder.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in setOrder.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "setOrder" ---
    for thisComponent in setOrder.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for setOrder
    setOrder.tStop = globalClock.getTime(format='float')
    setOrder.tStopRefresh = tThisFlipGlobal
    thisExp.addData('setOrder.stopped', setOrder.tStop)
    thisExp.nextEntry()
    # the Routine "setOrder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_loop = data.TrialHandler2(
        name='main_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'image_table.csv', 
        selection=selected_rows_str
    )
    , 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(main_loop)  # add the loop to the experiment
    thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            globals()[paramName] = thisMain_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_loop in main_loop:
        main_loop.status = STARTED
        if hasattr(thisMain_loop, 'status'):
            thisMain_loop.status = STARTED
        currentLoop = main_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
        if thisMain_loop != None:
            for paramName in thisMain_loop:
                globals()[paramName] = thisMain_loop[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[text_fixation],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
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
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixation* updates
            
            # if text_fixation is starting this frame...
            if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixation.frameNStart = frameN  # exact frame index
                text_fixation.tStart = t  # local t and not account for scr refresh
                text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fixation.started')
                # update status
                text_fixation.status = STARTED
                text_fixation.setAutoDraw(True)
            
            # if text_fixation is active this frame...
            if text_fixation.status == STARTED:
                # update params
                pass
            
            # if text_fixation is stopping this frame...
            if text_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixation.tStop = t  # not accounting for scr refresh
                    text_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    text_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_fixation.stopped')
                    # update status
                    text_fixation.status = FINISHED
                    text_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "ratingTrial" ---
        # create an object to store info about Routine ratingTrial
        ratingTrial = data.Routine(
            name='ratingTrial',
            components=[productImage, questionText, ratingValueText, ratingSlider, sliderCover, ratingMouse, leftAnchor, rightAnchor, warningText],
        )
        ratingTrial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from ratingCode
        questions_list = all_questions.copy()
        random.shuffle(questions_list)
        
        question_index = 0
        trial_ratings = {}
        trial_rts = {}
        trial_init = {}
        
        questionText.text = questions_list[question_index][1]
        
        # random initial mouse x position along the slider
        start_x = random.uniform(-SLIDER_WIDTH / 2, SLIDER_WIDTH / 2)
        ratingMouse.setPos((start_x, -0.33))
        
        # convert initial mouse position to 0-7 value
        init_val = ((start_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN
        init_val = round(init_val, 1)
        init_val = min(max(init_val, SLIDER_MIN), SLIDER_MAX)
        ratingSlider.reset()
        ratingSlider.markerPos = init_val
        ratingValueText.text = f"Rating: {init_val:.1f}"
        
        trial_init[questions_list[question_index][0]] = init_val
        
        questionClock.reset()
        click_ready = True
        waiting_next_question = False
        normal_delay = 0.5
        warning_delay = 1.5
        delay_duration = normal_delay
        sliderCover.opacity = 0
        warningText.opacity = 0
        timeout_warning = False
        productImage.setImage(image_path)
        ratingSlider.reset()
        # setup some python lists for storing info about the ratingMouse
        ratingMouse.x = []
        ratingMouse.y = []
        ratingMouse.leftButton = []
        ratingMouse.midButton = []
        ratingMouse.rightButton = []
        ratingMouse.time = []
        gotValidClick = False  # until a click is received
        # store start times for ratingTrial
        ratingTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ratingTrial.tStart = globalClock.getTime(format='float')
        ratingTrial.status = STARTED
        thisExp.addData('ratingTrial.started', ratingTrial.tStart)
        ratingTrial.maxDuration = None
        # keep track of which components have finished
        ratingTrialComponents = ratingTrial.components
        for thisComponent in ratingTrial.components:
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
        
        # --- Run Routine "ratingTrial" ---
        thisExp.currentRoutine = ratingTrial
        ratingTrial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from ratingCode
            # 1. Update positions
            mouse_x = ratingMouse.getPos()[0]
            current_val = ((mouse_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN
            current_val = min(max(round(current_val, 1), SLIDER_MIN), SLIDER_MAX)
            mouse_pressed = ratingMouse.getPressed()[0]
            
            # 2. Black screen / Warning delay state
            if waiting_next_question:
                productImage.opacity = 0
                questionText.text = ""
                ratingValueText.text = ""
                leftAnchor.text = ""
                rightAnchor.text = ""
                sliderCover.opacity = 1
                
                if timeout_warning:
                    warningText.opacity = 1
                    warningText.text = "Please answer before 8 seconds"
                else:
                    warningText.opacity = 0
            
                if delayClock.getTime() >= delay_duration:
                    waiting_next_question = False
                    
                    # Check if we should end the routine now
                    if question_index >= len(questions_list):
                        continueRoutine = False
                    else:
                        # Only run this if there IS a next question
                        productImage.opacity = 1
                        warningText.opacity = 0
                        sliderCover.opacity = 0
                        leftAnchor.text = "Not at all"
                        rightAnchor.text = "Very much"
                        questionText.text = questions_list[question_index][1]
            
                        start_x = random.uniform(-SLIDER_WIDTH / 2, SLIDER_WIDTH / 2)
                        ratingMouse.setPos((start_x, -0.33))
            
                        init_val = ((start_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN
                        init_val = min(max(round(init_val, 1), SLIDER_MIN), SLIDER_MAX)
            
                        ratingSlider.reset()
                        ratingSlider.markerPos = init_val
                        ratingValueText.text = f"Rating: {init_val:.1f}"
                        trial_init[questions_list[question_index][0]] = init_val
                        questionClock.reset()
            
            # 3. Normal question state
            else:
                productImage.opacity = 1
                leftAnchor.text = "Not at all"
                rightAnchor.text = "Very much"
                ratingSlider.markerPos = current_val
                ratingValueText.text = f"Rating: {current_val:.1f}"
            
                # Check for timeout
                if questionClock.getTime() >= TIME_LIMIT:
                    q_name = questions_list[question_index][0]
                    trial_ratings[q_name] = None
                    trial_rts[q_name] = None
                    timeout_warning = True
                    delay_duration = warning_delay
                    question_index += 1
                    waiting_next_question = True
                    delayClock.reset()
            
                # Check for click confirmation
                elif mouse_pressed and click_ready:
                    click_ready = False
                    q_name = questions_list[question_index][0]
                    trial_ratings[q_name] = current_val
                    trial_rts[q_name] = questionClock.getTime()
                    timeout_warning = False
                    delay_duration = normal_delay
                    question_index += 1
                    waiting_next_question = True
                    delayClock.reset()
            
            # re-arm click
            if not mouse_pressed:
                click_ready = True
            
            # *productImage* updates
            
            # if productImage is starting this frame...
            if productImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                productImage.frameNStart = frameN  # exact frame index
                productImage.tStart = t  # local t and not account for scr refresh
                productImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(productImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'productImage.started')
                # update status
                productImage.status = STARTED
                productImage.setAutoDraw(True)
            
            # if productImage is active this frame...
            if productImage.status == STARTED:
                # update params
                pass
            
            # *questionText* updates
            
            # if questionText is starting this frame...
            if questionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionText.frameNStart = frameN  # exact frame index
                questionText.tStart = t  # local t and not account for scr refresh
                questionText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'questionText.started')
                # update status
                questionText.status = STARTED
                questionText.setAutoDraw(True)
            
            # if questionText is active this frame...
            if questionText.status == STARTED:
                # update params
                pass
            
            # *ratingValueText* updates
            
            # if ratingValueText is starting this frame...
            if ratingValueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratingValueText.frameNStart = frameN  # exact frame index
                ratingValueText.tStart = t  # local t and not account for scr refresh
                ratingValueText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingValueText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ratingValueText.started')
                # update status
                ratingValueText.status = STARTED
                ratingValueText.setAutoDraw(True)
            
            # if ratingValueText is active this frame...
            if ratingValueText.status == STARTED:
                # update params
                pass
            
            # *ratingSlider* updates
            
            # if ratingSlider is starting this frame...
            if ratingSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratingSlider.frameNStart = frameN  # exact frame index
                ratingSlider.tStart = t  # local t and not account for scr refresh
                ratingSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ratingSlider.started')
                # update status
                ratingSlider.status = STARTED
                ratingSlider.setAutoDraw(True)
            
            # if ratingSlider is active this frame...
            if ratingSlider.status == STARTED:
                # update params
                pass
            
            # *sliderCover* updates
            
            # if sliderCover is starting this frame...
            if sliderCover.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sliderCover.frameNStart = frameN  # exact frame index
                sliderCover.tStart = t  # local t and not account for scr refresh
                sliderCover.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sliderCover, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sliderCover.started')
                # update status
                sliderCover.status = STARTED
                sliderCover.setAutoDraw(True)
            
            # if sliderCover is active this frame...
            if sliderCover.status == STARTED:
                # update params
                pass
            # *ratingMouse* updates
            
            # if ratingMouse is starting this frame...
            if ratingMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ratingMouse.frameNStart = frameN  # exact frame index
                ratingMouse.tStart = t  # local t and not account for scr refresh
                ratingMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ratingMouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ratingMouse.started', t)
                # update status
                ratingMouse.status = STARTED
                ratingMouse.mouseClock.reset()
                prevButtonState = ratingMouse.getPressed()  # if button is down already this ISN'T a new click
            if ratingMouse.status == STARTED:  # only update if started and not finished!
                buttons = ratingMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = ratingMouse.getPos()
                        ratingMouse.x.append(float(x))
                        ratingMouse.y.append(float(y))
                        buttons = ratingMouse.getPressed()
                        ratingMouse.leftButton.append(buttons[0])
                        ratingMouse.midButton.append(buttons[1])
                        ratingMouse.rightButton.append(buttons[2])
                        ratingMouse.time.append(ratingMouse.mouseClock.getTime())
            
            # *leftAnchor* updates
            
            # if leftAnchor is starting this frame...
            if leftAnchor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftAnchor.frameNStart = frameN  # exact frame index
                leftAnchor.tStart = t  # local t and not account for scr refresh
                leftAnchor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftAnchor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'leftAnchor.started')
                # update status
                leftAnchor.status = STARTED
                leftAnchor.setAutoDraw(True)
            
            # if leftAnchor is active this frame...
            if leftAnchor.status == STARTED:
                # update params
                pass
            
            # *rightAnchor* updates
            
            # if rightAnchor is starting this frame...
            if rightAnchor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightAnchor.frameNStart = frameN  # exact frame index
                rightAnchor.tStart = t  # local t and not account for scr refresh
                rightAnchor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightAnchor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rightAnchor.started')
                # update status
                rightAnchor.status = STARTED
                rightAnchor.setAutoDraw(True)
            
            # if rightAnchor is active this frame...
            if rightAnchor.status == STARTED:
                # update params
                pass
            
            # *warningText* updates
            
            # if warningText is starting this frame...
            if warningText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                warningText.frameNStart = frameN  # exact frame index
                warningText.tStart = t  # local t and not account for scr refresh
                warningText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(warningText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'warningText.started')
                # update status
                warningText.status = STARTED
                warningText.setAutoDraw(True)
            
            # if warningText is active this frame...
            if warningText.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ratingTrial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ratingTrial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ratingTrial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ratingTrial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ratingTrial" ---
        for thisComponent in ratingTrial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ratingTrial
        ratingTrial.tStop = globalClock.getTime(format='float')
        ratingTrial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ratingTrial.stopped', ratingTrial.tStop)
        # Run 'End Routine' code from ratingCode
        thisExp.addData('liking', trial_ratings.get('liking'))
        thisExp.addData('liking_initMouse', trial_init.get('liking'))
        thisExp.addData('liking_RT', trial_rts.get('liking'))
        
        thisExp.addData('taste', trial_ratings.get('taste'))
        thisExp.addData('taste_initMouse', trial_init.get('taste'))
        thisExp.addData('taste_RT', trial_rts.get('taste'))
        
        thisExp.addData('health', trial_ratings.get('health'))
        thisExp.addData('health_initMouse', trial_init.get('health'))
        thisExp.addData('health_RT', trial_rts.get('health'))
        main_loop.addData('ratingSlider.response', ratingSlider.getRating())
        main_loop.addData('ratingSlider.rt', ratingSlider.getRT())
        # store data for main_loop (TrialHandler)
        main_loop.addData('ratingMouse.x', ratingMouse.x)
        main_loop.addData('ratingMouse.y', ratingMouse.y)
        main_loop.addData('ratingMouse.leftButton', ratingMouse.leftButton)
        main_loop.addData('ratingMouse.midButton', ratingMouse.midButton)
        main_loop.addData('ratingMouse.rightButton', ratingMouse.rightButton)
        main_loop.addData('ratingMouse.time', ratingMouse.time)
        # the Routine "ratingTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "memoryTrial" ---
        # create an object to store info about Routine memoryTrial
        memoryTrial = data.Routine(
            name='memoryTrial',
            components=[memoryQuestion, opt1Text, opt2Text, opt3Text, memoryKey],
        )
        memoryTrial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from memoryCode
        # count how many times we've seen this product so far
        if product_id in memory_counts:
            memory_counts[product_id] += 1
        thisExp.addData('memory_count_now', memory_counts.get(product_id, ''))
        thisExp.addData('memory_target_now', memory_target_occurrence.get(product_id, ''))
        
        # choose whether to show the memory trial
        show_memory = False
        memory_correct_product = ""
        
        # show memory on the randomly chosen occurrence for each trigger product
        if product_id in MEMORY_TRIGGERS:
            if memory_counts[product_id] == memory_target_occurrence[product_id]:
                show_memory = True
                memory_correct_product = product_id
        
        # skip the routine unless this is a memory trial
        if not show_memory:
            continueRoutine = False
        else:
            wrong_options = random.sample(
                [p for p in all_products if p != memory_correct_product],
                2
            )
            memory_options = wrong_options + [memory_correct_product]
            random.shuffle(memory_options)
        
            memoryQuestion.text = "Which product was shown in the previous trial?\n\nUse keys 1, 2, or 3 to respond."
            opt1Text.text = "1. " + memory_options[0]
            opt2Text.text = "2. " + memory_options[1]
            opt3Text.text = "3. " + memory_options[2]
        
        # create starting attributes for memoryKey
        memoryKey.keys = []
        memoryKey.rt = []
        _memoryKey_allKeys = []
        # store start times for memoryTrial
        memoryTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        memoryTrial.tStart = globalClock.getTime(format='float')
        memoryTrial.status = STARTED
        thisExp.addData('memoryTrial.started', memoryTrial.tStart)
        memoryTrial.maxDuration = None
        # keep track of which components have finished
        memoryTrialComponents = memoryTrial.components
        for thisComponent in memoryTrial.components:
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
        
        # --- Run Routine "memoryTrial" ---
        thisExp.currentRoutine = memoryTrial
        memoryTrial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_loop, 'status') and thisMain_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *memoryQuestion* updates
            
            # if memoryQuestion is starting this frame...
            if memoryQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                memoryQuestion.frameNStart = frameN  # exact frame index
                memoryQuestion.tStart = t  # local t and not account for scr refresh
                memoryQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(memoryQuestion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'memoryQuestion.started')
                # update status
                memoryQuestion.status = STARTED
                memoryQuestion.setAutoDraw(True)
            
            # if memoryQuestion is active this frame...
            if memoryQuestion.status == STARTED:
                # update params
                pass
            
            # *opt1Text* updates
            
            # if opt1Text is starting this frame...
            if opt1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt1Text.frameNStart = frameN  # exact frame index
                opt1Text.tStart = t  # local t and not account for scr refresh
                opt1Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt1Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt1Text.started')
                # update status
                opt1Text.status = STARTED
                opt1Text.setAutoDraw(True)
            
            # if opt1Text is active this frame...
            if opt1Text.status == STARTED:
                # update params
                pass
            
            # *opt2Text* updates
            
            # if opt2Text is starting this frame...
            if opt2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt2Text.frameNStart = frameN  # exact frame index
                opt2Text.tStart = t  # local t and not account for scr refresh
                opt2Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt2Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt2Text.started')
                # update status
                opt2Text.status = STARTED
                opt2Text.setAutoDraw(True)
            
            # if opt2Text is active this frame...
            if opt2Text.status == STARTED:
                # update params
                pass
            
            # *opt3Text* updates
            
            # if opt3Text is starting this frame...
            if opt3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt3Text.frameNStart = frameN  # exact frame index
                opt3Text.tStart = t  # local t and not account for scr refresh
                opt3Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt3Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt3Text.started')
                # update status
                opt3Text.status = STARTED
                opt3Text.setAutoDraw(True)
            
            # if opt3Text is active this frame...
            if opt3Text.status == STARTED:
                # update params
                pass
            
            # *memoryKey* updates
            waitOnFlip = False
            
            # if memoryKey is starting this frame...
            if memoryKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                memoryKey.frameNStart = frameN  # exact frame index
                memoryKey.tStart = t  # local t and not account for scr refresh
                memoryKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(memoryKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'memoryKey.started')
                # update status
                memoryKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(memoryKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(memoryKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if memoryKey.status == STARTED and not waitOnFlip:
                theseKeys = memoryKey.getKeys(keyList=['1', '2', '3'], ignoreKeys=["escape"], waitRelease=False)
                _memoryKey_allKeys.extend(theseKeys)
                if len(_memoryKey_allKeys):
                    memoryKey.keys = _memoryKey_allKeys[-1].name  # just the last key pressed
                    memoryKey.rt = _memoryKey_allKeys[-1].rt
                    memoryKey.duration = _memoryKey_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=memoryTrial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                memoryTrial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if memoryTrial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in memoryTrial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "memoryTrial" ---
        for thisComponent in memoryTrial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for memoryTrial
        memoryTrial.tStop = globalClock.getTime(format='float')
        memoryTrial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('memoryTrial.stopped', memoryTrial.tStop)
        # Run 'End Routine' code from memoryCode
        
        if show_memory:
            if memoryKey.keys == '1':
                chosen_product = memory_options[0]
            elif memoryKey.keys == '2':
                chosen_product = memory_options[1]
            elif memoryKey.keys == '3':
                chosen_product = memory_options[2]
            else:
                chosen_product = ''
                
            memory_accuracy = int(chosen_product == memory_correct_product)
            thisExp.addData('memory_correct_product', memory_correct_product)
            thisExp.addData('memory_chosen', chosen_product)
            thisExp.addData('memory_accuracy', memory_accuracy)
            thisExp.addData('memory_RT', memoryKey.rt)
        else:
            thisExp.addData('memory_correct_product', '')
            thisExp.addData('memory_chosen', '')
            thisExp.addData('memory_accuracy', '')
            thisExp.addData('memory_RT', '')
        # check responses
        if memoryKey.keys in ['', [], None]:  # No response was made
            memoryKey.keys = None
        main_loop.addData('memoryKey.keys',memoryKey.keys)
        if memoryKey.keys != None:  # we had a response
            main_loop.addData('memoryKey.rt', memoryKey.rt)
            main_loop.addData('memoryKey.duration', memoryKey.duration)
        # the Routine "memoryTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisMain_loop as finished
        if hasattr(thisMain_loop, 'status'):
            thisMain_loop.status = FINISHED
        # if awaiting a pause, pause now
        if main_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            main_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'main_loop'
    main_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[endText, endKey],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for endKey
    endKey.keys = []
    endKey.rt = []
    _endKey_allKeys = []
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
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
    
    # --- Run Routine "thanks" ---
    thisExp.currentRoutine = thanks
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endText* updates
        
        # if endText is starting this frame...
        if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endText.frameNStart = frameN  # exact frame index
            endText.tStart = t  # local t and not account for scr refresh
            endText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endText.started')
            # update status
            endText.status = STARTED
            endText.setAutoDraw(True)
        
        # if endText is active this frame...
        if endText.status == STARTED:
            # update params
            pass
        
        # *endKey* updates
        waitOnFlip = False
        
        # if endKey is starting this frame...
        if endKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endKey.frameNStart = frameN  # exact frame index
            endKey.tStart = t  # local t and not account for scr refresh
            endKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endKey.started')
            # update status
            endKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endKey.status == STARTED and not waitOnFlip:
            theseKeys = endKey.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _endKey_allKeys.extend(theseKeys)
            if len(_endKey_allKeys):
                endKey.keys = _endKey_allKeys[-1].name  # just the last key pressed
                endKey.rt = _endKey_allKeys[-1].rt
                endKey.duration = _endKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            thanks.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if thanks.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # check responses
    if endKey.keys in ['', [], None]:  # No response was made
        endKey.keys = None
    thisExp.addData('endKey.keys',endKey.keys)
    if endKey.keys != None:  # we had a response
        thisExp.addData('endKey.rt', endKey.rt)
        thisExp.addData('endKey.duration', endKey.duration)
    thisExp.nextEntry()
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
