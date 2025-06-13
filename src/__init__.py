from src.VideoCaptureFromMediaPipe import detect_faces

def main():
    response = input("Would you like to start face detection? (y/n): ").strip().lower()
    if response == 'y':
        print("Face detection started. Press ESC to exit.")
        detect_faces()
    else:
        print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()
