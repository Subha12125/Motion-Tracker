# Motion-Tracker
# Background Subtraction using OpenCV MOG2

This project uses OpenCV's `BackgroundSubtractorMOG2` to detect moving objects in a video stream (from webcam or video file) by separating foreground from background in real-time.

## 📹 Features

- Real-time video processing using OpenCV.
- Background subtraction using Gaussian Mixture-based Background/Foreground Segmentation Algorithm (MOG2).
- Auto-restart video on end.
- Adjustable sensitivity with `history` and `varThreshold`.

## 🛠️ Requirements

- Python 3.x
- OpenCV (`cv2`)

Install OpenCV using pip:

```bash
pip install opencv-python
