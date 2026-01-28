import mediapipe as mp
try:
    print(f"Solutions: {mp.solutions}")
    print("Success")
except AttributeError as e:
    print(f"Error: {e}")
    import numpy
    print(f"Numpy version: {numpy.__version__}")
