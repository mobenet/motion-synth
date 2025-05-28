# Hand Tracking OSC

This project captures hand motion from a webcam and sends the distance between thumb and index finger via OSC to any audio or visual software.

## Features

- Real-time hand tracking with MediaPipe
- Sends distance data over OSC
- Designed to work with webcam or iPhone cam (via iVCam)

## Requirements

- Python 3.10
- mediapipe
- opencv-python
- python-osc

## How to run

1. Clone this repo
2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate it:

    ```bash
    .\venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the script:

    ```bash
    python hand_tracking.py
    ```

6. Press `q` to quit.

## OSC Output

- Address: `/handDistance`
- Port: `8000`
- Format: float (e.g., 137.4)

---

Feel free to use this motion data in Pure Data, SuperCollider, Processing, Unity, etc.
