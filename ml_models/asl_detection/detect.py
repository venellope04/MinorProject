import cv2
import numpy as np
from tensorflow.keras.models import load_model

def detect_asl(frame, model):
    # Preprocess the frame
    processed_frame = cv2.resize(frame, (64, 64))
    processed_frame = np.expand_dims(processed_frame, axis=0)
    processed_frame = processed_frame / 255.0

    # Predict the sign
    prediction = model.predict(processed_frame)
    return np.argmax(prediction, axis=1)[0]