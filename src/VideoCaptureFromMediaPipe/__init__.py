import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_faces():
    cap = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Skipping empty frame.")
                continue

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image_rgb)

            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)

            try:
                cv2.imshow("MediaPipe Face Detection", cv2.flip(image, 1))
            except cv2.error:
                print("Window was closed manually.")
                break

            if cv2.waitKey(5) & 0xFF == 27:  # ESC key
                break

    cap.release()
    cv2.destroyAllWindows()
