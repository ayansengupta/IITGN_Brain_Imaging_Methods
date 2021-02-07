# Download the Linux installer of Miniconda:

- Go to the website: https://docs.conda.io/en/latest/miniconda.html and navigate to linux installer section and download the latest python installer

# Install from WSL:

- navigate to the downloads folder on your C: Drive and run the installer

```bash

   bash /mnt/c/Users/<User>/Downloads/Miniconda3-latest-Linux-x86_64.sh
```

# Create a new environment

- To create a new conda virtual environement

```bash
   conda create -n <name_of_the_environment>
```


- For the image processing virtual environment the command to use is

```bash
   conda create -n image_processing
```
# Activate the environment 

- To activate the environment run the following command:

```bash
   conda activate image_processing
```

- The BASH prompt should show the activated environment label on the left. For example in my computer after activating it shows the following:


```bash
   (image_processing) spark@dell-spark:~$
```

# Install packages in the environment

- After activating the image_processing conda virtual environment, the required python packages required for the image processing tasks needs to be installed. This is very similar to installing specific MATLAB toolboxes. I mentioned this aimilarity/correspondence for students who are migrating to Python from MATLAB. In order to install required python packages (numpy, scipy, matplotlib), please run the following commands

```bash
   conda install numpy scipy matplotlib
```


# De-activate the environment 

- To deactivate the environment run the following command:

```bash
   conda deactivate image_processing
```










