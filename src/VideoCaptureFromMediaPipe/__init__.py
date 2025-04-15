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
                print("Ignorando frames em branco")
                continue

            # Converting the image from OpenCV standard to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Applying the image to the network
            results = face_detection.process(image_rgb)

            # Drawing the faces detected in the image
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)

            # Presenting the result
            cv2.imshow("MediaPipe Face Detection", cv2.flip(image, 1))

            if cv2.waitKey(5) & 0xFF == 27:  # ESC
                break

    # Release webcam device after loop
    cap.release()
    cv2.destroyAllWindows()
