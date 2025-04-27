# import libs 
## cv2: OpenCV to capture webcam image
## mediapipe: capture hand and landmarks
## udp_client: sends distance via message OSC
import cv2
import mediapipe as mp
import math
from pythonosc import udp_client

# Inicialitza Mediapipe
mp_hands = mp.solutions.hands
# mp_hands.Hands() create the hand detector
hands = mp_hands.Hands()
# to draw points and lines
mp_draw = mp.solutions.drawing_utils

# Inicialitza client OSC
client = udp_client.SimpleUDPClient("127.0.0.1", 8000)  # IP local i port 8000

# Captura de la webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame from camera")
        break
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibuixa els landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Agafa coordenades del polze i de l'índex
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Multipliquem els valors normalitzats per l'amplada (w) i l'alçada (h) de la imatge per obtenir coordenades reals en píxels.
            h, w, c = img.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            # Calcula la distància
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # Envia per OSC
            client.send_message("/handDistance", distance)

            # Mostra la distància a la imatge
            cv2.putText(img, f'Dist: {int(distance)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 2)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
