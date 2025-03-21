import cv2
import numpy as np
from ultralytics import __version__ as ultralytics_version
from sklearn import __version__ as sklearn_version

print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)
print("Ultralytics YOLO version:", ultralytics_version)
print("Scikit-learn version:", sklearn_version)
