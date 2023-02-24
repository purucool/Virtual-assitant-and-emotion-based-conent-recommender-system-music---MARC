from deepface import DeepFace
import cv2
def capture():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite("image1.png", image)
        cv2.waitKey(0)
    return image
def emotion_retriver():
    image = capture()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for x,y,w,h in face:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    try:
        analyze1 = DeepFace.analyze(image)
        return(analyze1['dominant_emotion'])
    except:
        return("no emotion")