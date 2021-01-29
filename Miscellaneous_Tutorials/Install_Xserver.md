# Download and install Xming exe file from sourceforge

https://sourceforge.net/projects/xming/

The checkbox should be checked in the last installation screen to launch the XServer. 


# In ubuntu shell add the following to use the Xming display 

```bash
 echo "export DISPLAY=localhost:0.0" >> ~/.bashrc
```
- try running 'gedit' to see if your xming is setup properly
