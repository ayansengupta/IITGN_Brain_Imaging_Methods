# System Requirements

    - Windows SUbsystem Linux on WIndows 10 with working Xming.
    
# Download Installer

  - https://fsl.fmrib.ox.ac.uk/fsldownloads_registration
  
# run downloaded script in Ubuntu shell via

 ```bash
 python /mnt/c/Users/<WindowsUserName>/Downloads/fslinstaller.py
```
Say yes to all default install options

# In ubuntu shell add

```bash
 echo "export DISPLAY=localhost:0.0" >> ~/.bashrc
```
- try running fslmaths, fsl, fsleyes. If fsleyes doesn't start, with a message referring to: libgtk-x11-2.0.so.0, then you will need to run:

```bash
sudo apt-get install libgtk2.0-0
```

- If fslmaths doesn't start, with a message referring to: libquadmath.so.0, then you will need to run (in case you didn't install it earlier):

```bash
 sudo apt-get install libquadmath0
```
- Please install firefox for showing results

 ```bash
 sudo apt-get install firefox
 ```


# Download the dataset

Navigate to the required folder where you want to keep your data

 ```
 cd /mnt/c/Users/<WindowsUserName>/Documents/
```

Then use the following command to download and store the data in gzip format. Use WinRar or other software to extract the data

```wget -c http://fsl.fmrib.ox.ac.uk/fslcourse/downloads/fmri1.tar.gz  
```


