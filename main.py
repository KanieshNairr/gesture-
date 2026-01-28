import cv2
import mediapipe as mp
import time

def main():  
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Hand Gesture Recognition Started. Press 'q' to exit.")

    while True:
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        gesture_name = "Unknown"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm_list = []
                h, w, c = img.shape
                for id, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
                
                if lm_list:
                    fingers = []
                    if lm_list[4][1] < lm_list[3][1]: 
                         fingers.append(1)
                    else:
                         fingers.append(0)
                    for id in [8, 12, 16, 20]:
                        if lm_list[id][2] < lm_list[id - 2][2]: 
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    total_fingers = fingers.count(1)
                    main_fingers = fingers[1:]
                    main_count = main_fingers.count(1)

                    if main_count == 0:
                        gesture_name = "Fist Bump"
                    elif main_count == 4:
                        if fingers[0]:
                            gesture_name = "Hello"
                        else:
                             gesture_name = "Salute"
                    elif main_fingers == [1, 0, 0, 0]: 
                        gesture_name = "Pointing"
                    elif main_fingers == [1, 1, 0, 0]: 
                        gesture_name = "Peace"
                    elif main_fingers == [0, 0, 0, 1]:
                        gesture_name = "Promise"
                    elif main_fingers == [1, 0, 0, 1]: 
                        gesture_name = "Rock n Roll"
                        
                    # React
                    print(f"Detected: {gesture_name}")
                    
        # Display Gesture Name
        cv2.rectangle(img, (0,0), (640, 60), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, f"Gesture: {gesture_name}", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Hand Gesture Recognition", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
