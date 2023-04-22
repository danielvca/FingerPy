import cv2
import vlc
import time
import mediapipe as mp
import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def hand_or_finger_detected(landmarks):
    return True if landmarks else False

def main():
    video_path = "C:\\PROJECTS\\Finger\\cars.mp4"
    player = vlc.MediaPlayer(video_path)
    player.play()

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB and process the image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)

            # Check if a hand or finger is detected
            if results.multi_hand_landmarks and hand_or_finger_detected(results.multi_hand_landmarks):
                if player.get_state() != vlc.State.Paused:
                    player.set_fullscreen(True)
                    player.pause()
            else:
                if player.get_state() == vlc.State.Paused:
                    player.pause()

            if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
