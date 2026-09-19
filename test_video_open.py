# test_video_open.py
import cv2, os
path = "data/sample_weapon_video.mp4"
print("Checking path:", os.path.abspath(path))
if not os.path.exists(path):
    print("FILE MISSING:", path)
    raise SystemExit(1)

cap = cv2.VideoCapture(path)
print("isOpened():", cap.isOpened())
if not cap.isOpened():
    print("OpenCV couldn't open the file. Possible causes: unsupported codec or corrupted file.")
else:
    ret, frame = cap.read()
    print("read frame success:", ret)
    if ret:
        print("frame shape:", frame.shape)
        cv2.imwrite("data/test_first_frame.jpg", frame)
        print("Wrote data/test_first_frame.jpg")
cap.release()
