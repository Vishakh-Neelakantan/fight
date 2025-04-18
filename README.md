# 🛡️ Fight/Accident/Loitering Detection in Video using YOLOv8

This project is a computer vision system that utilizes the **YOLOv8** object detection model to identify specific events such as **fights**, **accidents**, and **loitering** in surveillance videos. The system processes video frames in real-time, detects relevant events, and highlights them with bounding boxes along with triggering console alerts.

---

## 📌 Features

- 🎯 Real-time object detection using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- 🔎 Focused on detecting fight, accident, and loitering behaviors
- ✅ Draws bounding boxes and class labels on the video feed
- 🚨 Console alerts when a suspicious event is detected

---

## 🛠️ Requirements

Ensure you have **Python 3.8+** installed. Then install the following dependencies:

```bash
pip install torch torchvision torchaudio
pip install ultralytics
pip install opencv-python-headless
```
---

## 🚀 How to Run
- Place your video (e.g., fightclip.mp4) in the same folder as the script.

- Ensure all dependencies are installed.

- Run the script using:

bash
Copy
Edit
python main.py

-A window will open showing the video with detections. Press q to exit.

---

## 🧠 Model
The model used is yolov8n.pt, a lightweight YOLOv8 model.

It is loaded using the Ultralytics YOLO API.

---

## 📦 Future Improvements
Train a custom YOLOv8 model specifically for "fight", "accident", and "loitering" classes.

Add sound or email-based alerting system.

Deploy the system for real-time CCTV streams.

---
