import cv2
import os
# from tkinter.filedialog import askopenfilename
from tkFileDialog import askopenfilename

AbsolutePath=os.getcwd()
file = open("nameOfVideos.txt", "r")
for filename in file:
    filename=filename.strip()
    VideoPath=os.path.join(AbsolutePath,"Videos", filename)
    video = cv2.VideoCapture(VideoPath)
    if not video.isOpened():
        print("file not valid")
        exit()
    success, image = video.read()
    count = 0
    success = True
    while success:
        cv2.imwrite(os.path.join(AbsolutePath,"Images",filename + "-frame%d.jpg" % count), image)
        success, image = video.read()
        if success:
            print('Reading frame', count+1)
        count += 1
