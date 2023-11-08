import cv2
import serial

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 represents the default camera

# Initialize the Arduino communication
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Adjust the port and baud rate as needed

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # Faces detected, send a signal to Arduino to turn on the LED
        arduino.write(b'1')
    else:
        # No faces detected, send a signal to Arduino to turn off the LED
        arduino.write(b'0')

    # Display the frame with rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()