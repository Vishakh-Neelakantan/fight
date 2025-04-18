# Install dependencies
# !pip install torch torchvision torchaudio
# !pip install ultralytics
# !pip install opencv-python-headless

# Import necessary libraries
import torch
from ultralytics import YOLO
import cv2
from google.colab.patches import cv2_imshow

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# # Mount Google Drive
# from google.colab import drive
# drive.mount('/content/drive')

# Define the path to your video file in Google Drive
video_path = 'fightclip.mp4'

# Define the function to process the video
def detect_events_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        # Process results and trigger alerts
        for result in results:
            for box in result.boxes:
                cls = int(box.cls)  # Assuming 'cls' is the label index
                label = model.names[cls]  # Map index to label name
                if label in ['fight', 'accident', 'loitering']:
                    # Trigger alert
                    print(f"Alert: {label} detected")
                # Draw bounding box and label
                x1, y1, x2, y2 = map(int, box.xyxy)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2_imshow(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

# Use the video file from Google Drive
detect_events_in_video(video_path)