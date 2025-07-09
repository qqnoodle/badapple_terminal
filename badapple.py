import cv2
import time

capture = cv2.VideoCapture("badapple.mp4")
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
resize_width = 80
resize_height = 80

asci = ["=", "@"]

for frame_number in range(frame_count):
    #frame_data is an numpy array
    successful_read, frame_data = capture.read()
    frame_data = cv2.resize(frame_data, (resize_width, resize_height))
    if not successful_read: 
        break
    out = ""
    for h in range(resize_height):
        for w in range(resize_width):
            #converts pixel into 1 or 0, 0 indicate black and 1 indicate white
            r,g,b = frame_data[h,w]
            color = int(r > 0)
            out += asci[color]
        out += "\n"
    print(out)
    time.sleep(1/60)

capture.release()