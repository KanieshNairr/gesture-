import sys
print(f"Python: {sys.version}")

try:
    import cv2
    print(f"OpenCV Version: {cv2.__version__}")
except ImportError as e:
    print(f"Failed to import cv2: {e}")

import mediapipe as mp
try:
    print(f"Solutions: {mp.solutions}")
    print("MediaPipe Success")
except AttributeError as e:
    print(f"MediaPipe Error: {e}")
