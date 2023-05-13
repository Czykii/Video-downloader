# Video-downloader
 
## **1. Introduction**
This project is a python application to download videos and playlists from YouTube.

----------
<br>

## **2. Getting started**
To run the program you'll need to install
* Python 3.X
* Tkinter library
* Pytube library

To install tkinter use command:

```
pip install tk
```

To install pytube use command:
```
python -m pip install git+https://github.com/pytube/pytube
```
<!---
To make this app work flawlessly make sure to change line 223 of file **innertube.py** from:
``` python
def __init__(self, client='ANDROID_MUSIC', use_oauth=False, allow_cache=True):
```
to:
``` python
def __init__(self, client='WEB', use_oauth=False, allow_cache=True):
```
--->

## **3. Use of the application**
To run the app, simply run the main.py file after cloning or downloading the repository and installing the libraries (if you don't have them already installed).
<br>

To use the app you need to choose what do you want do download (single video or a playlist), next place the link to it to the input field. Make sure, that the video(s) that you want to download **isn't private**. The video(s) will be downloaded in the localization of the main.py file.

----------
<br>