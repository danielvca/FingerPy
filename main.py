import cv2
import vlc
import time
import os
import glob
import mediapipe as mp
import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection

def hand_near_head(landmarks, face_landmarks):
    if not face_landmarks:
        return False

    nose_x, nose_y = face_landmarks[0].x, face_landmarks[0].y
    threshold = 0.15

    for i in [0, 4, 8, 12, 16, 20]:
        x, y = landmarks[i].x, landmarks[i].y
        if abs(nose_x - x) < threshold and abs(nose_y - y) < threshold:
            return True

    return False

def play_video(video_path):
    player = vlc.MediaPlayer(video_path)
    player.play()

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands, \
         mp_face.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB and process the image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            hand_results = hands.process(image)
            face_results = face_detection.process(image)

            face_landmarks = None
            if face_results.detections:
                face_landmarks = face_results.detections[0].location_data.relative_keypoints

            # Check if a hand is detected near the head
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    if hand_near_head(hand_landmarks.landmark, face_landmarks):
                        if player.get_state() != vlc.State.Paused:
                            player.set_fullscreen(True)
                            player.pause()
                    else:
                        if player.get_state() == vlc.State.Paused:
                            player.pause()

            if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit
                player.stop()
                break

            if player.get_state() == vlc.State.Ended:
                break

    cap.release()
    cv2.destroyAllWindows()

def main():
    video_folder = "C:\\PROJECTS\\Finger\\"
    video_files = glob.glob(os.path.join(video_folder, "*.mp4"))

    for video_path in video_files:
        print(f"Playing {video_path}")
        play_video(video_path)

# Call the main function directly
main()
