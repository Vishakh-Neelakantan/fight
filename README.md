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

---