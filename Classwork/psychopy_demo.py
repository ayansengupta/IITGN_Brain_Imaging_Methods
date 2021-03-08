from psychopy import visual, core, logging, event  # import some libraries from PsychoPy, include logging for creating logfiles
from datetime import datetime # import datetime library for timestamp
from psychopy.hardware import keyboard # import keyboard library

# Set logging level and create log file

# this is for displaying logs on the console, if needed can be commented out
#logging.console.setLevel(logging.EXP)

# getting the timestamp and including it into the logfile name
timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
lastLog = logging.LogFile("lastRun_"+timestamp+".log", level=logging.INFO, filemode='w')

# create keyboard object
kb = keyboard.Keyboard()


#create a window
#the demo monitor specs are as follows 
#Aspect Ratio (pixel): 1024 x 768
#Screen width (cm): 30
#screen distance (cm): 30

mywin = visual.Window([800,600], monitor="demo_monitor", units="deg")


#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=5, pos=[-8,5], sf=3)

#introduced a gabor grating
#it is a sine grating with a gaussian on top
gabor_grating = visual.GratingStim(win=mywin, mask="gauss", size=10, pos=[8,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#introduce an image as a stimulation
iitgn_logo = visual.ImageStim(win=mywin, image="Psychopy_IITGN_Logo.png", size=5, pos=[-8,-5], units="deg")

#draw the stimuli and update the window
grating.draw()
iitgn_logo.draw()
gabor_grating.draw()
fixation.draw()
mywin.update()

#pause, so you get a chance to see it!
core.wait(5.0)
logging.flush()

# creating static stimulation by looping over frames
frame_refresh=50
trial_duration=10
number_of_trials=1
total_frames=frame_refresh*trial_duration*number_of_trials

for frameN in range(total_frames):
    grating.draw()
    gabor_grating.draw()
    iitgn_logo.draw()
    fixation.draw()
    mywin.update()
    logging.flush()

    
    
# creating the dynamic stimulation by modifying phase of the gratings
for frameN in range(total_frames):
    
    grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
    gabor_grating.setPhase(0.05, '-')
    grating.draw()
    gabor_grating.draw()
    iitgn_logo.draw()
    fixation.draw()
    mywin.update()
    logging.flush()
    
    
    
# creating the dynamic flickering stimulation with 50% duty cycle
# Screen refresh rate is 50 (50 frames in 1 sec), which means for 50% duty cycle the stimulation is ON for 25 frames and OFF for 25 frames

for frameN in range(total_frames):
    iitgn_logo.draw()
    fixation.draw()

    if (frameN % frame_refresh) < 25 :     # ON phase
        grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
        gabor_grating.setPhase(0.05, '-')
        grating.draw()
        gabor_grating.draw()
        mywin.update()
    else: # OFF phase
        mywin.update()
      
    logging.flush()

### set up a realistic experiment

Participant_Instruction = visual.TextStim(mywin, 'Welcome, Are you ready?', color=(0, 1, 0), colorSpace='rgb')    
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['1', '2'])
print(Subject_Response)
if '1' in Subject_Response:

    # Scanner waiting instruction
    scanner_wait = visual.TextStim(mywin, 'Great, Waiting for Scanner Trigger', color=(0, 1, 0), colorSpace='rgb')    
    scanner_wait.draw()
    mywin.update()

    keys = event.waitKeys(keyList=['t'])
    
    for frameN in range(total_frames):
    
        grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
        gabor_grating.setPhase(0.05, '-')
        
        fixation.draw()
        grating.draw()
        iitgn_logo.draw()
        
        if (frameN % frame_refresh) < 25 :     # ON phase
            gabor_grating.draw()
            mywin.update()
        else: # OFF phase
            mywin.update()
          
        logging.flush()  

    Participant_Instruction.setText('Did the gabor grating flicker?')
    Participant_Instruction.draw()
    mywin.update()
    Subject_Response = event.waitKeys(keyList=['1', '2'])

    for frameN in range(total_frames):
    
        grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
        gabor_grating.setPhase(0.05, '-')
        
        fixation.draw()
        gabor_grating.draw()
        iitgn_logo.draw()
        
        if (frameN % frame_refresh) < 25 :     # ON phase
            grating.draw()
            mywin.update()
        else: # OFF phase
            mywin.update()
          
        logging.flush()  

    Participant_Instruction.setText('Did the sine grating flicker?')
    Participant_Instruction.draw()
    mywin.update()
    Subject_Response = event.waitKeys(keyList=['1', '2'])
    
    Participant_Instruction.setText('End of the Experiment. Thank you')
    Participant_Instruction.draw()
    mywin.update()
    core.wait(5)