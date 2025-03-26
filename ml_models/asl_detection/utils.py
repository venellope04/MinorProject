import cv2
import numpy as np

def preprocess_frame(frame):
    """
    Preprocess the input frame to match the model's expected input (64x64 RGB).
    
    Args:
        frame (np.ndarray): Input frame as a NumPy array (BGR format from OpenCV).
    
    Returns:
        np.ndarray: Preprocessed frame ready for model input.
    """
    # Resize to model input size (64x64)
    target_size = (64, 64)
    resized_frame = cv2.resize(frame, target_size)
    
    # Convert BGR to RGB (TensorFlow models expect RGB)
    rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    
    # Normalize pixel values to [0, 1] (matches training preprocessing)
    normalized_frame = rgb_frame / 255.0
    
    # Ensure the frame has the correct shape (height, width, channels)
    if len(normalized_frame.shape) == 3 and normalized_frame.shape[2] == 3:
        return normalized_frame
    else:
        raise ValueError("Invalid frame shape after preprocessing")