REQUIREMENTS:
============

* Python 3 (tested on Python 3.6.5).
* OpenCV for Face Detection.
* pygame for making window.
* OS: Built entirely on Ubuntu 18.04.


HOW TO RUN:
==========
* Open terminal change directory to location where these files are located.
* run command './face_track.py'(without quotes).

TO ADD YOUR OWN IMAGES:
======================
* Remove background using image editing software like GIMP.
* Remove eyes from the image and store in the different file.
* Now you have to change the value of variables img_x, img_y in function show.
* To change background just change the value of bg variable to you favorite color's rgb.

(Added Windows Support but I don't have a windows machine so can't test.)


