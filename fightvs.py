import torch
from ultralytics import YOLO
import cv2

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Define the path to your video file
video_path = 'fightclip.mp4'

# Define the function to process the video
def detect_events_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        for result in results:
            for box in result.boxes:
                cls = int(box.cls)
                label = model.names[cls]
                if label in ['fight', 'accident', 'loitering']:
                    print(f"Alert: {label} detected")
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Call the function
detect_events_in_video(video_path)
