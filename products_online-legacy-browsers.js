/************************ 
 * Products_Online *
 ************************/


// store info about the experiment session:
let expName = 'products_online';  // from the Builder filename that created this script
let expInfo = {
    'participant_ID': '',
    'age': '',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(setOrderRoutineBegin());
flowScheduler.add(setOrderRoutineEachFrame());
flowScheduler.add(setOrderRoutineEnd());
const main_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(main_loopLoopBegin(main_loopLoopScheduler));
flowScheduler.add(main_loopLoopScheduler);
flowScheduler.add(main_loopLoopEnd);




flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'image_table.csv', 'path': 'image_table.csv'},
    {'name': 'taste&health/Allin_original.png', 'path': 'taste&health/Allin_original.png'},
    {'name': 'taste&health/Allin_taste.png', 'path': 'taste&health/Allin_taste.png'},
    {'name': 'taste&health/Allin_health.png', 'path': 'taste&health/Allin_health.png'},
    {'name': 'taste&health/Cheetos_original.png', 'path': 'taste&health/Cheetos_original.png'},
    {'name': 'taste&health/Cheetos_taste.png', 'path': 'taste&health/Cheetos_taste.png'},
    {'name': 'taste&health/Cheetos_health.png', 'path': 'taste&health/Cheetos_health.png'},
    {'name': 'taste&health/ChocolatePara_original.png', 'path': 'taste&health/ChocolatePara_original.png'},
    {'name': 'taste&health/ChocolatePara_taste.png', 'path': 'taste&health/ChocolatePara_taste.png'},
    {'name': 'taste&health/ChocolatePara_health.png', 'path': 'taste&health/ChocolatePara_health.png'},
    {'name': 'taste&health/CocaColaZero_original.png', 'path': 'taste&health/CocaColaZero_original.png'},
    {'name': 'taste&health/CocaColaZero_taste.png', 'path': 'taste&health/CocaColaZero_taste.png'},
    {'name': 'taste&health/CocaColaZero_health.png', 'path': 'taste&health/CocaColaZero_health.png'},
    {'name': 'taste&health/Cornflakes_original.png', 'path': 'taste&health/Cornflakes_original.png'},
    {'name': 'taste&health/Cornflakes_taste.png', 'path': 'taste&health/Cornflakes_taste.png'},
    {'name': 'taste&health/Cornflakes_health.png', 'path': 'taste&health/Cornflakes_health.png'},
    {'name': 'taste&health/MangoFree_original.png', 'path': 'taste&health/MangoFree_original.png'},
    {'name': 'taste&health/MangoFree_taste.png', 'path': 'taste&health/MangoFree_taste.png'},
    {'name': 'taste&health/MangoFree_health.png', 'path': 'taste&health/MangoFree_health.png'},
    {'name': 'taste&health/Nutella_original.png', 'path': 'taste&health/Nutella_original.png'},
    {'name': 'taste&health/Nutella_taste.png', 'path': 'taste&health/Nutella_taste.png'},
    {'name': 'taste&health/Nutella_health.png', 'path': 'taste&health/Nutella_health.png'},
    {'name': 'taste&health/Slimdelis_original.png', 'path': 'taste&health/Slimdelis_original.png'},
    {'name': 'taste&health/Slimdelis_taste.png', 'path': 'taste&health/Slimdelis_taste.png'},
    {'name': 'taste&health/Slimdelis_health.png', 'path': 'taste&health/Slimdelis_health.png'},
    {'name': 'taste&health/Tamar_original.png', 'path': 'taste&health/Tamar_original.png'},
    {'name': 'taste&health/Tamar_taste.png', 'path': 'taste&health/Tamar_taste.png'},
    {'name': 'taste&health/Tamar_health.png', 'path': 'taste&health/Tamar_health.png'},
    {'name': 'taste&health/Tapuchips_original.png', 'path': 'taste&health/Tapuchips_original.png'},
    {'name': 'taste&health/Tapuchips_taste.png', 'path': 'taste&health/Tapuchips_taste.png'},
    {'name': 'taste&health/Tapuchips_health.png', 'path': 'taste&health/Tapuchips_health.png'},
    {'name': 'taste&health/TimTam_original.png', 'path': 'taste&health/TimTam_original.png'},
    {'name': 'taste&health/TimTam_taste.png', 'path': 'taste&health/TimTam_taste.png'},
    {'name': 'taste&health/TimTam_health.png', 'path': 'taste&health/TimTam_health.png'},
    {'name': 'taste&health/WaffleCrisp_original.png', 'path': 'taste&health/WaffleCrisp_original.png'},
    {'name': 'taste&health/WaffleCrisp_taste.png', 'path': 'taste&health/WaffleCrisp_taste.png'},
    {'name': 'taste&health/WaffleCrisp_health.png', 'path': 'taste&health/WaffleCrisp_health.png'},
    {'name': 'taste&health/XL_original.png', 'path': 'taste&health/XL_original.png'},
    {'name': 'taste&health/XL_taste.png', 'path': 'taste&health/XL_taste.png'},
    {'name': 'taste&health/XL_health.png', 'path': 'taste&health/XL_health.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant_ID"]}/${expInfo["participant_ID"]}_${expName}_${expInfo["date"].split("_")[0]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var text_welcome;
var key_resp;
var instructionsClock;
var text_instructions;
var key_resp_instructions;
var setOrderClock;
var fixationClock;
var text_fixation;
var ratingTrialClock;
var TTIME_LIMIT;
var all_questions;
var SLIDER_MIN;
var SLIDER_MAX;
var SLIDER_WIDTH;
var SLIDER_Y;
var questionClock;
var delayClock;
var waiting_next_question;
var timeout_warning;
var click_ready;
var question_index;
var current_x;
var delay_duration;
var normal_delay;
var warning_delay;
var productImage;
var questionText;
var ratingValueText;
var ratingSlider;
var sliderCover;
var ratingMouse;
var leftAnchor;
var rightAnchor;
var warningText;
var memoryTrialClock;
var MEMORY_TRIGGERS;
var memory_counts;
var memory_target_occurrence;
var all_products;
var memoryQuestion;
var opt1Text;
var opt2Text;
var opt3Text;
var memoryKey;
var thanksClock;
var endText;
var endKey;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  text_welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_welcome',
    text: 'Welcome!\nThis is a decision-making experiment\nPress SPACE to start',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instructions',
    text: 'INSTRUCTIONS:\nPlease answer these 3 questions:\n- How much do you LIKE the product?\n- How TASTY do you think the product is?\n- How HEALTHY do you think the product is?\n\nRate each question from 0 (not at all) to 7 (very much).\n\nUse the mouse to move the slider and click to confirm your rating.\nYou will have 8 seconds to answer each question.\n\nPress SPACE to begin the experiment',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_instructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "setOrder"
  setOrderClock = new util.Clock();
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  text_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ratingTrial"
  ratingTrialClock = new util.Clock();
  // Run 'Begin Experiment' code from ratingCode
  TTIME_LIMIT = 8;
  
  all_questions = [
    ["liking", "How much do you LIKE the product?"],
    ["taste", "How TASTY do you think the product is?"],
    ["health", "How HEALTHY do you think the product is?"]
  ];
  
  SLIDER_MIN = 0;
  SLIDER_MAX = 7;
  SLIDER_WIDTH = 0.72;
  SLIDER_Y = -0.33;
  
  questionClock = new util.Clock();
  delayClock = new util.Clock();
  
  waiting_next_question = false;
  timeout_warning = false;
  click_ready = false;
  question_index = 0;
  current_x = 0;
  
  delay_duration = 0.5;
  normal_delay = 0.5;
  warning_delay = 1.5;
  productImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'productImage', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.14], 
    draggable: false,
    size : [0.6, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  questionText = new visual.TextStim({
    win: psychoJS.window,
    name: 'questionText',
    text: 'placeholder',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.22)], draggable: false, height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  ratingValueText = new visual.TextStim({
    win: psychoJS.window,
    name: 'ratingValueText',
    text: 'Rating:',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.26)], draggable: false, height: 0.028,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  ratingSlider = new visual.Slider({
    win: psychoJS.window, name: 'ratingSlider',
    startValue: undefined,
    size: [0.7, 0.05], pos: [0, (- 0.33)], ori: 0.0, units: psychoJS.window.units,
    labels: [0, 1, 2, 3, 4, 5, 6, 7], fontSize: 0.05, ticks: [0, 1, 2, 3, 4, 5, 6, 7],
    granularity: 0.1, style: ["SLIDER"],
    color: new util.Color('white'), markerColor: new util.Color('white'), lineColor: new util.Color('white'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: false,
  });
  
  sliderCover = new visual.Rect ({
    win: psychoJS.window, name: 'sliderCover', 
    width: [0.8, 0.18][0], height: [0.8, 0.18][1],
    ori: 0.0, 
    pos: [0, (- 0.36)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('black'), 
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -5, 
    interpolate: true, 
  });
  
  ratingMouse = new core.Mouse({
    win: psychoJS.window,
  });
  ratingMouse.mouseClock = new util.Clock();
  leftAnchor = new visual.TextStim({
    win: psychoJS.window,
    name: 'leftAnchor',
    text: 'Not at all',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), (- 0.44)], draggable: false, height: 0.022,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  rightAnchor = new visual.TextStim({
    win: psychoJS.window,
    name: 'rightAnchor',
    text: 'Very much',
    font: 'Arial',
    units: undefined, 
    pos: [0.35, (- 0.44)], draggable: false, height: 0.022,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  warningText = new visual.TextStim({
    win: psychoJS.window,
    name: 'warningText',
    text: 'Please answer before 8 seconds',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "memoryTrial"
  memoryTrialClock = new util.Clock();
  // Run 'Begin Experiment' code from memoryCode
  MEMORY_TRIGGERS = {"Tapuchips": 1, "Nutella": 1, "Cheetos": 1, "CocaColaZero": 1};
  memory_counts = {"Tapuchips": 0, "Nutella": 0, "Cheetos": 0, "CocaColaZero": 0};
  memory_target_occurrence = {};
  
  var product_list = ["Tapuchips", "Nutella", "Cheetos", "CocaColaZero"];
  var occurrences = [1, 2, 3];
  
  for (var i = 0; i < product_list.length; i++) {
      var prod = product_list[i];
      
      // Manual random choice: Pick a random index from the [1, 2, 3] array
      var randomIndex = Math.floor(Math.random() * occurrences.length);
      memory_target_occurrence[prod] = occurrences[randomIndex];
  }
  
  all_products = ["Allin", "Cheetos", "ChocolatePara", "CocaColaZero", "Cornflakes", "MangoFree", "Nutella", "Slimdelis", "Tamar", "Tapuchips", "TimTam", "WaffleCrisp", "XL"];
  memoryQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'memoryQuestion',
    text: 'Which product was shown in the previous trial?\n\nUse keys 1, 2, or 3 to respond',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  opt1Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt1Text',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  opt2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt2Text',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  opt3Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt3Text',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.15)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  memoryKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: 'Thank you!\nPress SPACE to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  endKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var WelcomeMaxDurationReached;
var _key_resp_allKeys;
var WelcomeMaxDuration;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    WelcomeClock.reset();
    routineTimer.reset();
    WelcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    WelcomeMaxDuration = null
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(text_welcome);
    WelcomeComponents.push(key_resp);
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_welcome* updates
    if (t >= 0.0 && text_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_welcome.tStart = t;  // (not accounting for frame time here)
      text_welcome.frameNStart = frameN;  // exact frame index
      
      text_welcome.setAutoDraw(true);
    }
    
    
    // if text_welcome is active this frame...
    if (text_welcome.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionsMaxDurationReached;
var _key_resp_instructions_allKeys;
var instructionsMaxDuration;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionsClock.reset();
    routineTimer.reset();
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_instructions.keys = undefined;
    key_resp_instructions.rt = undefined;
    _key_resp_instructions_allKeys = [];
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text_instructions);
    instructionsComponents.push(key_resp_instructions);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_instructions* updates
    if (t >= 0.0 && text_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instructions.tStart = t;  // (not accounting for frame time here)
      text_instructions.frameNStart = frameN;  // exact frame index
      
      text_instructions.setAutoDraw(true);
    }
    
    
    // if text_instructions is active this frame...
    if (text_instructions.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_instructions* updates
    if (t >= 0.0 && key_resp_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_instructions.tStart = t;  // (not accounting for frame time here)
      key_resp_instructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_instructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instructions.clearEvents(); });
    }
    
    // if key_resp_instructions is active this frame...
    if (key_resp_instructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_instructions.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp_instructions_allKeys = _key_resp_instructions_allKeys.concat(theseKeys);
      if (_key_resp_instructions_allKeys.length > 0) {
        key_resp_instructions.keys = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].name;  // just the last key pressed
        key_resp_instructions.rt = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].rt;
        key_resp_instructions.duration = _key_resp_instructions_allKeys[_key_resp_instructions_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_instructions.corr, level);
    }
    psychoJS.experiment.addData('key_resp_instructions.keys', key_resp_instructions.keys);
    if (typeof key_resp_instructions.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_instructions.rt', key_resp_instructions.rt);
        psychoJS.experiment.addData('key_resp_instructions.duration', key_resp_instructions.duration);
        routineTimer.reset();
        }
    
    key_resp_instructions.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var setOrderMaxDurationReached;
var all_trials;
var row_order;
var selected_rows_str;
var setOrderMaxDuration;
var setOrderComponents;
function setOrderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'setOrder' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    setOrderClock.reset();
    routineTimer.reset();
    setOrderMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_serOrder
    all_trials = TrialHandler.importConditions(psychoJS.serverManager, 'image_table.csv');
    row_order = [...Array(all_trials.length).keys()];
    
    function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }
    
    let valid_order = false;
    while (!valid_order) {
      shuffleArray(row_order);
      valid_order = true;
      for (let i = 0; i < row_order.length - 1; i++) {
        if (all_trials[row_order[i]]["product_id"] === all_trials[row_order[i + 1]]["product_id"]) {
          valid_order = false;
          break;
        }
      }
    }
    
    selected_rows_str = row_order.join(",");
    continueRoutine = false;
    psychoJS.experiment.addData('setOrder.started', globalClock.getTime());
    setOrderMaxDuration = null
    // keep track of which components have finished
    setOrderComponents = [];
    
    setOrderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setOrderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'setOrder' ---
    // get current time
    t = setOrderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setOrderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setOrderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'setOrder' ---
    setOrderComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('setOrder.stopped', globalClock.getTime());
    // the Routine "setOrder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var main_loop;
function main_loopLoopBegin(main_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    main_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'image_table.csv', selected_rows_str),
      seed: undefined, name: 'main_loop'
    });
    psychoJS.experiment.addLoop(main_loop); // add the loop to the experiment
    currentLoop = main_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    main_loop.forEach(function() {
      snapshot = main_loop.getSnapshot();
    
      main_loopLoopScheduler.add(importConditions(snapshot));
      main_loopLoopScheduler.add(fixationRoutineBegin(snapshot));
      main_loopLoopScheduler.add(fixationRoutineEachFrame());
      main_loopLoopScheduler.add(fixationRoutineEnd(snapshot));
      main_loopLoopScheduler.add(ratingTrialRoutineBegin(snapshot));
      main_loopLoopScheduler.add(ratingTrialRoutineEachFrame());
      main_loopLoopScheduler.add(ratingTrialRoutineEnd(snapshot));
      main_loopLoopScheduler.add(memoryTrialRoutineBegin(snapshot));
      main_loopLoopScheduler.add(memoryTrialRoutineEachFrame());
      main_loopLoopScheduler.add(memoryTrialRoutineEnd(snapshot));
      main_loopLoopScheduler.add(main_loopLoopEndIteration(main_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function main_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(main_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function main_loopLoopEndIteration(scheduler, snapshot) {
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


var fixationMaxDurationReached;
var fixationMaxDuration;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fixationClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(text_fixation);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fixation* updates
    if (t >= 0.0 && text_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fixation.tStart = t;  // (not accounting for frame time here)
      text_fixation.frameNStart = frameN;  // exact frame index
      
      text_fixation.setAutoDraw(true);
    }
    
    
    // if text_fixation is active this frame...
    if (text_fixation.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_fixation.tStop = t;  // not accounting for scr refresh
      text_fixation.frameNStop = frameN;  // exact frame index
      // update status
      text_fixation.status = PsychoJS.Status.FINISHED;
      text_fixation.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fixationMaxDurationReached) {
        fixationClock.add(fixationMaxDuration);
    } else {
        fixationClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ratingTrialMaxDurationReached;
var questions_list;
var trial_ratings;
var trial_rts;
var trial_init;
var init_val;
var gotValidClick;
var ratingTrialMaxDuration;
var ratingTrialComponents;
function ratingTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ratingTrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    ratingTrialClock.reset();
    routineTimer.reset();
    ratingTrialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from ratingCode
    questions_list = [...all_questions];
    document.body.style.cursor = 'none';
    // Fisher-Yates shuffle
    for (let i = questions_list.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [questions_list[i], questions_list[j]] = [questions_list[j], questions_list[i]];
    }
    question_index = 0;
    trial_ratings = {};
    trial_rts = {};
    trial_init = {};
    // initial UI
    questionText.text = questions_list[question_index][1];
    sliderCover.opacity = 0.0;
    warningText.opacity = 0.0;
    productImage.opacity = 1.0;
    leftAnchor.text = "Not at all";
    rightAnchor.text = "Very much";
    
    // random initial slider position
    let start_x = (Math.random() * SLIDER_WIDTH) - (SLIDER_WIDTH / 2);
    current_x = start_x;
    let init_val = ((current_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN;
    init_val = Math.min(Math.max(Number.parseFloat(init_val.toFixed(1)), SLIDER_MIN), SLIDER_MAX);
    
    ratingSlider.reset();
    ratingSlider.markerPos = init_val;
    ratingValueText.text = "Rating: " + init_val.toFixed(1);
    
    trial_init[questions_list[question_index][0]] = init_val;
    
    // state
    waiting_next_question = false;
    timeout_warning = false;
    click_ready = false;
    questionClock.reset();
    delayClock.reset();
    productImage.setImage(image_path);
    ratingSlider.reset()
    // setup some python lists for storing info about the ratingMouse
    // current position of the mouse:
    ratingMouse.x = [];
    ratingMouse.y = [];
    ratingMouse.leftButton = [];
    ratingMouse.midButton = [];
    ratingMouse.rightButton = [];
    ratingMouse.time = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('ratingTrial.started', globalClock.getTime());
    ratingTrialMaxDuration = null
    // keep track of which components have finished
    ratingTrialComponents = [];
    ratingTrialComponents.push(productImage);
    ratingTrialComponents.push(questionText);
    ratingTrialComponents.push(ratingValueText);
    ratingTrialComponents.push(ratingSlider);
    ratingTrialComponents.push(sliderCover);
    ratingTrialComponents.push(ratingMouse);
    ratingTrialComponents.push(leftAnchor);
    ratingTrialComponents.push(rightAnchor);
    ratingTrialComponents.push(warningText);
    
    ratingTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var current_val;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function ratingTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ratingTrial' ---
    // get current time
    t = ratingTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from ratingCode
    
    // 1. Get mouse / slider state
    let mousePos = ratingMouse.getPos();
    let mouse_pressed = ratingMouse.getPressed()[0] === 1;
    
    // only allow a click after mouse has been released
    if (!mouse_pressed) {
        click_ready = true;
    }
    
    // update current_x only if mouse actually moved
    if (mousePos && Math.abs(mousePos[0]) > 0.001) {
        current_x = mousePos[0];
    }
    
    // clamp x to slider width
    current_x = Math.max(-SLIDER_WIDTH / 2, Math.min(SLIDER_WIDTH / 2, current_x));
    
    // convert x to slider value
    let current_val = ((current_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN;
    current_val = Math.min(Math.max(Number.parseFloat(current_val.toFixed(1)), SLIDER_MIN), SLIDER_MAX);
    
    // 2. Delay / blackout state
    if (waiting_next_question) {
        productImage.opacity = 0.0;
        questionText.text = "";
        ratingValueText.text = "";
        leftAnchor.text = "";
        rightAnchor.text = "";
        sliderCover.opacity = 1.0;
    
        if (timeout_warning) {
            warningText.text = "Please answer before 8 seconds";
            warningText.opacity = 1.0;
        } else {
            warningText.opacity = 0.0;
        }
    
        // after delay, move to next question
        if (delayClock.getTime() >= delay_duration) {
            if (question_index >= questions_list.length) {
                continueRoutine = false;
            } else {
                waiting_next_question = false;
                timeout_warning = false;
    
                productImage.opacity = 1.0;
                warningText.opacity = 0.0;
                sliderCover.opacity = 0.0;
    
                leftAnchor.text = "Not at all";
                rightAnchor.text = "Very much";
                questionText.text = questions_list[question_index][1];
    
                // random start for next question
                let next_start_x = (Math.random() * SLIDER_WIDTH) - (SLIDER_WIDTH / 2);
                current_x = next_start_x;
    
                let next_init_val = ((current_x + SLIDER_WIDTH / 2) / SLIDER_WIDTH) * (SLIDER_MAX - SLIDER_MIN) + SLIDER_MIN;
                next_init_val = Math.min(Math.max(Number.parseFloat(next_init_val.toFixed(1)), SLIDER_MIN), SLIDER_MAX);
    
                ratingSlider.reset();
                ratingSlider.markerPos = next_init_val;
                ratingValueText.text = "Rating: " + next_init_val.toFixed(1);
    
                trial_init[questions_list[question_index][0]] = next_init_val;
    
                questionClock.reset();
            }
        }
    }
    // 3. Active question state
    else {
        sliderCover.opacity = 0.0;
        warningText.opacity = 0.0;
        productImage.opacity = 1.0;
    
        leftAnchor.text = "Not at all";
        rightAnchor.text = "Very much";
    
        ratingSlider.markerPos = current_val;
        ratingValueText.text = "Rating: " + current_val.toFixed(1);
    
        // timeout
        if (questionClock.getTime() >= TTIME_LIMIT) {
            let q_name = questions_list[question_index][0];
            trial_ratings[q_name] = null;
            trial_rts[q_name] = null;
    
            timeout_warning = true;
            delay_duration = warning_delay;
            question_index += 1;
            waiting_next_question = true;
            delayClock.reset();
        }
        // click
        else if (mouse_pressed && click_ready) {
            click_ready = false;
    
            let q_name = questions_list[question_index][0];
            trial_ratings[q_name] = current_val;
            trial_rts[q_name] = questionClock.getTime();
    
            timeout_warning = false;
            delay_duration = normal_delay;
            question_index += 1;
            waiting_next_question = true;
            delayClock.reset();
        }
    }
    
    // *productImage* updates
    if (t >= 0.0 && productImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      productImage.tStart = t;  // (not accounting for frame time here)
      productImage.frameNStart = frameN;  // exact frame index
      
      productImage.setAutoDraw(true);
    }
    
    
    // if productImage is active this frame...
    if (productImage.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *questionText* updates
    if (t >= 0.0 && questionText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      questionText.tStart = t;  // (not accounting for frame time here)
      questionText.frameNStart = frameN;  // exact frame index
      
      questionText.setAutoDraw(true);
    }
    
    
    // if questionText is active this frame...
    if (questionText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *ratingValueText* updates
    if (t >= 0.0 && ratingValueText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingValueText.tStart = t;  // (not accounting for frame time here)
      ratingValueText.frameNStart = frameN;  // exact frame index
      
      ratingValueText.setAutoDraw(true);
    }
    
    
    // if ratingValueText is active this frame...
    if (ratingValueText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *ratingSlider* updates
    if (t >= 0.0 && ratingSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingSlider.tStart = t;  // (not accounting for frame time here)
      ratingSlider.frameNStart = frameN;  // exact frame index
      
      ratingSlider.setAutoDraw(true);
    }
    
    
    // if ratingSlider is active this frame...
    if (ratingSlider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *sliderCover* updates
    if (t >= 0.0 && sliderCover.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sliderCover.tStart = t;  // (not accounting for frame time here)
      sliderCover.frameNStart = frameN;  // exact frame index
      
      sliderCover.setAutoDraw(true);
    }
    
    
    // if sliderCover is active this frame...
    if (sliderCover.status === PsychoJS.Status.STARTED) {
    }
    
    // *ratingMouse* updates
    if (t >= 0.0 && ratingMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ratingMouse.tStart = t;  // (not accounting for frame time here)
      ratingMouse.frameNStart = frameN;  // exact frame index
      
      ratingMouse.status = PsychoJS.Status.STARTED;
      ratingMouse.mouseClock.reset();
      prevButtonState = ratingMouse.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if ratingMouse is active this frame...
    if (ratingMouse.status === PsychoJS.Status.STARTED) {
      _mouseButtons = ratingMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = ratingMouse.getPos();
          ratingMouse.x.push(_mouseXYs[0]);
          ratingMouse.y.push(_mouseXYs[1]);
          ratingMouse.leftButton.push(_mouseButtons[0]);
          ratingMouse.midButton.push(_mouseButtons[1]);
          ratingMouse.rightButton.push(_mouseButtons[2]);
          ratingMouse.time.push(ratingMouse.mouseClock.getTime());
        }
      }
    }
    
    // *leftAnchor* updates
    if (t >= 0.0 && leftAnchor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leftAnchor.tStart = t;  // (not accounting for frame time here)
      leftAnchor.frameNStart = frameN;  // exact frame index
      
      leftAnchor.setAutoDraw(true);
    }
    
    
    // if leftAnchor is active this frame...
    if (leftAnchor.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *rightAnchor* updates
    if (t >= 0.0 && rightAnchor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightAnchor.tStart = t;  // (not accounting for frame time here)
      rightAnchor.frameNStart = frameN;  // exact frame index
      
      rightAnchor.setAutoDraw(true);
    }
    
    
    // if rightAnchor is active this frame...
    if (rightAnchor.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *warningText* updates
    if (t >= 0.0 && warningText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warningText.tStart = t;  // (not accounting for frame time here)
      warningText.frameNStart = frameN;  // exact frame index
      
      warningText.setAutoDraw(true);
    }
    
    
    // if warningText is active this frame...
    if (warningText.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ratingTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ratingTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ratingTrial' ---
    ratingTrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ratingTrial.stopped', globalClock.getTime());
    // Run 'End Routine' code from ratingCode
    psychoJS.experiment.addData("liking", trial_ratings["liking"]);
    psychoJS.experiment.addData("liking_initMouse", trial_init["liking"]);
    psychoJS.experiment.addData("liking_RT", trial_rts["liking"]);
    
    psychoJS.experiment.addData("taste", trial_ratings["taste"]);
    psychoJS.experiment.addData("taste_initMouse", trial_init["taste"]);
    psychoJS.experiment.addData("taste_RT", trial_rts["taste"]);
    
    psychoJS.experiment.addData("health", trial_ratings["health"]);
    psychoJS.experiment.addData("health_initMouse", trial_init["health"]);
    psychoJS.experiment.addData("health_RT", trial_rts["health"]);
    psychoJS.experiment.addData('ratingSlider.response', ratingSlider.getRating());
    psychoJS.experiment.addData('ratingSlider.rt', ratingSlider.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('ratingMouse.x', ratingMouse.x);
    psychoJS.experiment.addData('ratingMouse.y', ratingMouse.y);
    psychoJS.experiment.addData('ratingMouse.leftButton', ratingMouse.leftButton);
    psychoJS.experiment.addData('ratingMouse.midButton', ratingMouse.midButton);
    psychoJS.experiment.addData('ratingMouse.rightButton', ratingMouse.rightButton);
    psychoJS.experiment.addData('ratingMouse.time', ratingMouse.time);
    
    // the Routine "ratingTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var memoryTrialMaxDurationReached;
var _pj;
var show_memory;
var memory_correct_product;
var _memoryKey_allKeys;
var memoryTrialMaxDuration;
var memoryTrialComponents;
function memoryTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memoryTrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    memoryTrialClock.reset();
    routineTimer.reset();
    memoryTrialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from memoryCode
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    
    // Update memory count
    if (_pj.in_es6(product_id, memory_counts)) {
        memory_counts[product_id] += 1;
    }
    
    // Data logging
    psychoJS.experiment.addData("memory_count_now", memory_counts[product_id] || "");
    psychoJS.experiment.addData("memory_target_now", memory_target_occurrence[product_id] || "");
    
    show_memory = false;
    memory_correct_product = "";
    
    // Check if memory task should trigger
    if (_pj.in_es6(product_id, MEMORY_TRIGGERS)) {
        if ((memory_counts[product_id] === memory_target_occurrence[product_id])) {
            show_memory = true;
            memory_correct_product = product_id;
        }
    }
    
    if (!show_memory) {
        continueRoutine = false;
    } else {
        // 1. Hide mouse at start
        document.body.style.cursor = 'none';
        //interaction_started = false; 
    
        // 2. Generate the list of wrong options
        let distractor_pool = [];
        for (let p of all_products) {
            if (p !== memory_correct_product) {
                distractor_pool.push(p);
            }
        }
    
        // 3. Shuffle the pool manually and pick the first 2
        // (This is a native JS way to do a 'sample')
        distractor_pool.sort(() => Math.random() - 0.5);
        wrong_options = distractor_pool.slice(0, 2);
    
        // 4. Combine with the correct product
        memory_options = [wrong_options[0], wrong_options[1], memory_correct_product];
    
        // 5. Shuffle the final 3 options so the correct one moves
        memory_options.sort(() => Math.random() - 0.5);
    
        // 6. Update UI
        memoryQuestion.text = "Which product was shown in the previous trial?\n\nUse keys 1, 2, or 3 to respond.";
        opt1Text.text = ("1. " + memory_options[0]);
        opt2Text.text = ("2. " + memory_options[1]);
        opt3Text.text = ("3. " + memory_options[2]);
    }
        
    memoryKey.keys = undefined;
    memoryKey.rt = undefined;
    _memoryKey_allKeys = [];
    psychoJS.experiment.addData('memoryTrial.started', globalClock.getTime());
    memoryTrialMaxDuration = null
    // keep track of which components have finished
    memoryTrialComponents = [];
    memoryTrialComponents.push(memoryQuestion);
    memoryTrialComponents.push(opt1Text);
    memoryTrialComponents.push(opt2Text);
    memoryTrialComponents.push(opt3Text);
    memoryTrialComponents.push(memoryKey);
    
    memoryTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function memoryTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memoryTrial' ---
    // get current time
    t = memoryTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *memoryQuestion* updates
    if (t >= 0.0 && memoryQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      memoryQuestion.tStart = t;  // (not accounting for frame time here)
      memoryQuestion.frameNStart = frameN;  // exact frame index
      
      memoryQuestion.setAutoDraw(true);
    }
    
    
    // if memoryQuestion is active this frame...
    if (memoryQuestion.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *opt1Text* updates
    if (t >= 0.0 && opt1Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opt1Text.tStart = t;  // (not accounting for frame time here)
      opt1Text.frameNStart = frameN;  // exact frame index
      
      opt1Text.setAutoDraw(true);
    }
    
    
    // if opt1Text is active this frame...
    if (opt1Text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *opt2Text* updates
    if (t >= 0.0 && opt2Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opt2Text.tStart = t;  // (not accounting for frame time here)
      opt2Text.frameNStart = frameN;  // exact frame index
      
      opt2Text.setAutoDraw(true);
    }
    
    
    // if opt2Text is active this frame...
    if (opt2Text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *opt3Text* updates
    if (t >= 0.0 && opt3Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opt3Text.tStart = t;  // (not accounting for frame time here)
      opt3Text.frameNStart = frameN;  // exact frame index
      
      opt3Text.setAutoDraw(true);
    }
    
    
    // if opt3Text is active this frame...
    if (opt3Text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *memoryKey* updates
    if (t >= 0.0 && memoryKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      memoryKey.tStart = t;  // (not accounting for frame time here)
      memoryKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { memoryKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { memoryKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { memoryKey.clearEvents(); });
    }
    
    // if memoryKey is active this frame...
    if (memoryKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = memoryKey.getKeys({
        keyList: typeof ['1','2','3'] === 'string' ? [['1','2','3']] : ['1','2','3'], 
        waitRelease: false
      });
      _memoryKey_allKeys = _memoryKey_allKeys.concat(theseKeys);
      if (_memoryKey_allKeys.length > 0) {
        memoryKey.keys = _memoryKey_allKeys[_memoryKey_allKeys.length - 1].name;  // just the last key pressed
        memoryKey.rt = _memoryKey_allKeys[_memoryKey_allKeys.length - 1].rt;
        memoryKey.duration = _memoryKey_allKeys[_memoryKey_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    memoryTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var chosen_product;
var memory_accuracy;
function memoryTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memoryTrial' ---
    memoryTrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('memoryTrial.stopped', globalClock.getTime());
    // Run 'End Routine' code from memoryCode
    if (show_memory) {
        if ((memoryKey.keys === "1")) {
            chosen_product = memory_options[0];
        } else {
            if ((memoryKey.keys === "2")) {
                chosen_product = memory_options[1];
            } else {
                if ((memoryKey.keys === "3")) {
                    chosen_product = memory_options[2];
                } else {
                    chosen_product = "";
                }
            }
        }
        memory_accuracy = Number.parseInt((chosen_product === memory_correct_product));
        psychoJS.experiment.addData("memory_correct_product", memory_correct_product);
        psychoJS.experiment.addData("memory_chosen", chosen_product);
        psychoJS.experiment.addData("memory_accuracy", memory_accuracy);
        psychoJS.experiment.addData("memory_RT", memoryKey.rt);
    } else {
        psychoJS.experiment.addData("memory_correct_product", "");
        psychoJS.experiment.addData("memory_chosen", "");
        psychoJS.experiment.addData("memory_accuracy", "");
        psychoJS.experiment.addData("memory_RT", "");
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(memoryKey.corr, level);
    }
    psychoJS.experiment.addData('memoryKey.keys', memoryKey.keys);
    if (typeof memoryKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('memoryKey.rt', memoryKey.rt);
        psychoJS.experiment.addData('memoryKey.duration', memoryKey.duration);
        routineTimer.reset();
        }
    
    memoryKey.stop();
    // the Routine "memoryTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var thanksMaxDurationReached;
var _endKey_allKeys;
var thanksMaxDuration;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    thanksClock.reset();
    routineTimer.reset();
    thanksMaxDurationReached = false;
    // update component parameters for each repeat
    endKey.keys = undefined;
    endKey.rt = undefined;
    _endKey_allKeys = [];
    psychoJS.experiment.addData('thanks.started', globalClock.getTime());
    thanksMaxDuration = null
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(endText);
    thanksComponents.push(endKey);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
    }
    
    
    // if endText is active this frame...
    if (endText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *endKey* updates
    if (t >= 0.0 && endKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endKey.tStart = t;  // (not accounting for frame time here)
      endKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endKey.clearEvents(); });
    }
    
    // if endKey is active this frame...
    if (endKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = endKey.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _endKey_allKeys = _endKey_allKeys.concat(theseKeys);
      if (_endKey_allKeys.length > 0) {
        endKey.keys = _endKey_allKeys[_endKey_allKeys.length - 1].name;  // just the last key pressed
        endKey.rt = _endKey_allKeys[_endKey_allKeys.length - 1].rt;
        endKey.duration = _endKey_allKeys[_endKey_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endKey.corr, level);
    }
    psychoJS.experiment.addData('endKey.keys', endKey.keys);
    if (typeof endKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endKey.rt', endKey.rt);
        psychoJS.experiment.addData('endKey.duration', endKey.duration);
        routineTimer.reset();
        }
    
    endKey.stop();
    // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
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
