from psychopy import visual, core  # import some libraries from PsychoPy

#create a window
#the demo monitor specs are as follows 
#Aspect Ratio (pixel): 1024 x 768
#Screen width (cm): 30
#screen distance (cm): 30

mywin = visual.Window([800,600], monitor="demo_monitor", units="deg")


#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=10, pos=[-8,0], sf=3)

#introduced a gabor grating
#it is a sine grating with a gaussian on top
gabor_grating = visual.GratingStim(win=mywin, mask="gauss", size=10, pos=[8,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
grating.draw()
gabor_grating.draw()
fixation.draw()
mywin.update()

#pause, so you get a chance to see it!
core.wait(10.0)

# creating static stimulation by looping over frames
frame_refresh=50
trial_duration=10
number_of_trials=1
total_frames=frame_refresh*trial_duration*number_of_trials

for frameN in range(total_frames):
    grating.draw()
    gabor_grating.draw()
    fixation.draw()
    mywin.update()

    
    
# creating the dynamic stimulation by modifying phase of the gratings
for frameN in range(total_frames):
    
    grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
    gabor_grating.setPhase(0.05, '-')
    grating.draw()
    gabor_grating.draw()
    fixation.draw()
    mywin.update()
    
    
    
# creating the dynamic flickering stimulation with 50% duty cycle
# Screen refresh rate is 50 (50 frames in 1 sec), which means for 50% duty cycle the stimulation is ON for 25 frames and OFF for 25 frames

for frameN in range(total_frames):
    if (frameN % frame_refresh) < 25 :     # ON phase
        grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
        gabor_grating.setPhase(0.05, '-')
        grating.draw()
        gabor_grating.draw()
        fixation.draw()
        mywin.update()
    else: # OFF phase
        mywin.update()
    
    
    
