import sys
import pkg_resources

print(f"Python: {sys.version}")
try:
    import mediapipe
    print(f"MediaPipe path: {mediapipe.__file__}")
    print(f"Dir MediaPipe: {dir(mediapipe)}")
except ImportError as e:
    print(f"ImportError: {e}")

try:
    import google.protobuf
    print(f"Protobuf version: {google.protobuf.__version__}")
except ImportError:
    print("Protobuf not found")

try:
    from mediapipe.python import solutions
    print("Successfully imported mediapipe.python.solutions")
except ImportError as e:
    print(f"Failed to import mediapipe.python.solutions: {e}")

try:
    import mediapipe.python as mp_python
    print(f"Dir mp_python: {dir(mp_python)}")
except ImportError as e:
    print(f"Failed to import mediapipe.python: {e}")
