import os
import sys
import cv2
import numpy as np
import tensorflow as tf

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Add project root to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '../../'))
sys.path.append(project_root)
from ml_models.asl_detection.utils import preprocess_frame

# Path to your trained model (relative to project root)
MODEL_PATH = os.path.join(project_root, 'ml_models/asl_detection/asl_model.h5')
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully from", MODEL_PATH)
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

# Classes for ASL digits (0-9)
ASL_CLASSES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def detect_signs(frame):
    if model is None:
        print("Model not loaded. Returning '[None]'")
        return "[None]"

    try:
        processed_frame = preprocess_frame(frame)
        processed_frame = np.expand_dims(processed_frame, axis=0)
        predictions = model.predict(processed_frame, verbose=0)
        predicted_class_idx = np.argmax(predictions[0])
        if 0 <= predicted_class_idx < len(ASL_CLASSES):
            translation = ASL_CLASSES[predicted_class_idx]
        else:
            translation = "[Unknown]"
        print(f"Predicted class index: {predicted_class_idx}, Translation: {translation}")
        return translation
    except Exception as e:
        print(f"Error during detection: {e}")
        return "[Error]"

def test_detection():
    if model is None:
        print("Model not loaded. Cannot test.")
        return
    test_image_path = os.path.join(project_root, 'ml_models/asl_detection/test_image.jpg')
    test_frame = cv2.imread(test_image_path)
    if test_frame is None:
        print(f"Failed to load test image from {test_image_path}")
        return
    translation = detect_signs(test_frame)
    print(f"Test detection result: {translation}")

if __name__ == "__main__":
    test_detection()