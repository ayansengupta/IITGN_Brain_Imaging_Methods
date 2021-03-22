# HeuDiConv setup

1. Check whether you have a previously created heudiconv environment and whether the version of python you have used for the heudiconv environment is 3.7 or not. For doing that open a terminal and Use the following command. If you check the output, in this case line 3 shows that the python version is 3.7.10. 
   ```
   (base) spark@LAPTOP-UMDAETEC:~$ conda list -n heudiconv | grep "python"
   
      ipython                   7.21.0           py37h888b3d9_0    conda-forge
      ipython_genutils          0.2.0                      py_1    conda-forge
      python                    3.7.10               hdb3f193_0
      python-dateutil           2.8.1                      py_0    conda-forge
      python-utils              2.5.5              pyh44b312d_0    conda-forge
      python_abi                3.7                     1_cp37m    conda-forge
      wxpython                  4.0.4            py37hc99224d_0
      
   ```
2. If it is a newer version like 3.9 etc. Then you will have to delete this environment because of incompatibility with ```fsleyes```. You should remove your old conda env with the following 2 commands. 

   ```
   
   (base) spark@LAPTOP-UMDAETEC:~$ conda env list | grep heudiconv
   heudiconv                /home/spark/miniconda3/envs/heudiconv
   
   (base) spark@LAPTOP-UMDAETEC:~$  rm -r /home/spark/miniconda3/envs/heudiconv
   
   ```
   
3. Create a new heudiconv environment with python 3.7

   ```
   (base) spark@LAPTOP-UMDAETEC:~$ conda create -n heudiconv python=3.7
   ```
   
4. Activate the heudiconv environment, intall the heudiconv and fsleyes libraries.

   ```
   (base) spark@LAPTOP-UMDAETEC:~$ conda activate heudiconv
   (base) spark@LAPTOP-UMDAETEC:~$ conda install -c conda-forge heudiconv
   (base) spark@LAPTOP-UMDAETEC:~$ conda install -c conda-forge fsleyes
   
   ```
   
5. Generate the heuristic files and dicominfo.tsv file with the following command

   ```
   (base) spark@LAPTOP-UMDAETEC:~$ heudiconv -d /mnt/c/Users/User/Documents/Miscellaneous/sub-{subject}/ses-{session}/SCANS/6/DICOM/*.dcm -s 01 -ss 005 -f convertall -c none -o /mnt/c/Users/User/Documents/Miscellaneous/
   ```
   
6. After careful inspection of the diconminfo.tsv file, you will need to modify the ```heuristic_template.py``` file according to your requirements. The template file is provided at https://github.com/ayansengupta/IITGN_Brain_Imaging_Methods/blob/main/Miscellaneous_Tutorials/heuristic_template.py. 

7. The actual nifti conversion is done by the following command

   ```
   (base) spark@LAPTOP-UMDAETEC:~$ heudiconv -d /mnt/c/Users/User/Documents/Miscellaneous/Raw_Dicom/sub-{subject}/ses-{session}/SCANS/6/DICOM/*.dcm -s 01 -ss 005 -f       /mnt/c/Users/User/Documents/Miscellaneous/heuristic_template.py -c dcm2niix -b notop --overwrite -o /mnt/c/Users/User/Documents/Miscellaneous/

   ```
   
