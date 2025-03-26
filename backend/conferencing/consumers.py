import os
import sys
import cv2
import numpy as np
from channels.generic.websocket import AsyncWebsocketConsumer

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from ml_models.asl_detection.detect import detect_signs

class SignDetectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket connected for sign detection")

    async def disconnect(self, close_code):
        print("WebSocket disconnected")

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            try:
                # Decode the JPEG frame to OpenCV format
                nparr = np.frombuffer(bytes_data, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if frame is None:
                    print("Failed to decode frame")
                    await self.send(text_data="[None]")
                    return

                # Detect ASL sign
                translation = detect_signs(frame)
                # Send translation back to client
                await self.send(text_data=translation)
            except Exception as e:
                print(f"Error processing frame: {e}")
                await self.send(text_data="[Error]")