
# FingerPy - Mouth Detection and Video Control

written by Daniel Andrade. 

- https://azureblog.dev
- https://github.com/danielvca

## Overview

FingerPy is a Python application that plays video files and uses computer vision to automatically pause or resume playback based on hand gestures. Specifically, the application detects if the user places their hand near their head and pauses the video accordingly. Resuming playback is as simple as moving the hand away from the head.

## Dependencies

-   OpenCV (cv2)
-   Python-VLC (vlc)
-   time
-   os
-   glob
-   MediaPipe (mediapipe)
-   keyboard

To install these dependencies, use the following pip command:

`pip install opencv-python python-vlc mediapipe keyboard` 

## Code Structure

The code consists of three main functions:

1.  `hand_near_head(landmarks, face_landmarks)`: Determines if a hand is near the head based on the given landmarks.
2.  `play_video(video_path)`: Plays a video from the specified path and processes the hand gestures for controlling playback.
3.  `main()`: Searches for video files in the specified folder and plays them in order.

## Usage

To run FingerPy, simply execute the Python script with your preferred Python interpreter. For example:

`python fingerpy.py` 

The script will search for video files in the specified folder (`video_folder`) and play them one by one. While the video is playing, bring your hand close to your head to pause the video, and move it away to resume playback. To exit the application, press the 'ESC' key.

## Customization

You can change the `video_folder` variable in the `main()` function to point to your desired video folder. By default, the script searches for `.mp4` video files. To support other video formats, modify the file extension in the `glob.glob()` function call within the `main()` function.

> Written with [StackEdit](https://stackedit.io/).