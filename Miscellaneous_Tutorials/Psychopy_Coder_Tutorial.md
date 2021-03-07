# Create a static stimulation

See the following code for a static stimulation. Before the required libraries ```visual``` and ```core``` are imported from ```psychopy``` the important parameters for calculating the visual angle like monitor aspect ratio, screen width in cm and screen distance from the eyes are being input into the ```monitor centre``` of psychopy. The rest of the stimulus created will be created in terms of the visual angle.  

``` bash
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

```

The above code creates a stimulus that doesn't does not change over time. First a display window ```mywin``` is created with a size of 800X600 pixels on the demo_monitor with the following command. 

```mywin = visual.Window([800,600], monitor="demo_monitor", units="deg")```

Two different grating stimuli (sine and gabor) are created by the ```visual.GratingStim()``` function. 

```
#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=10, pos=[-8,0], sf=3)

#introduced a gabor grating
#it is a sine grating with a gaussian on top
gabor_grating = visual.GratingStim(win=mywin, mask="gauss", size=10, pos=[8,0], sf=3)
```

Fixation point is also created by the ```visual.GratingStim()``` function by modifying the spatial frequency to zero ```sf=0```.

After drawing the stimulation of the gratingstims on the window ```mywin```, it is updated with the ```mywin.update()``` command and then ```core.wait(10.0)``` keeps the stimulation on the screen for 10 sec.


# Create a static stimulation for-looping over frames


# Create a dynamic stimulation with gratings changing phase with time


# create a dynamic stimulation with flickering gratings


# Display Imagea as a stimulation


# Display instructions


# Create Log files


# Logging participant responses as Keyboard Inputs

# Modifying experiment control with while-loop and synchronizing with scanner-trigger

