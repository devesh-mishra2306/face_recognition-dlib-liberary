from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np

def detect(image):
    #image=image[:, :, ::-1]
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

    # Create a PIL imagedraw object so we can draw on the picture
    #pil_image = Image.fromarray(image)
    #d = ImageDraw.Draw(pil_image)
    
    for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    #for facial_feature in face_landmarks.keys():
     #   print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    #for facial_feature in face_landmarks.keys():
        #d.line(face_landmarks['left_eye'], width=5)
        #d.line(face_landmarks['right_eye'], width=5)
        my_eyel = np.asarray(face_landmarks['left_eye'])
        my_eyel=my_eyel.reshape(-1,1,2)
        cv2.drawContours(image, my_eyel, -1, (0,255,0), 2)
        
        my_eyer = np.asarray(face_landmarks['right_eye'])
        my_eyer=my_eyer.reshape(-1,1,2)
        cv2.drawContours(image, my_eyer, -1, (0,255,0), 2)
        
        my_upper = np.asarray(face_landmarks['top_lip'])
        my_upper=my_upper.reshape(-1,1,2)
        cv2.drawContours(image, my_upper, -1, (0,255,0), 2)
        
        
        my_lower = np.asarray(face_landmarks['bottom_lip'])
        my_lower=my_lower.reshape(-1,1,2)
        cv2.drawContours(image, my_lower, -1, (0,255,0), 2)
        
        nose_bridge = np.asarray(face_landmarks['nose_bridge'])
        nose_bridge=nose_bridge.reshape(-1,1,2)
        cv2.drawContours(image, nose_bridge, -1, (0,255,0), 2)
        
        nose_tip = np.asarray(face_landmarks['nose_tip'])
        nose_tip=nose_tip.reshape(-1,1,2)
        cv2.drawContours(image, nose_tip, -1, (0,255,0), 2)
        
        
        #myarrayr= 
    return image

#builiding for web cam
video_capture=cv2.VideoCapture(0)
while True:
    _,frame=video_capture.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(frame)
    cv2.imshow('video',canvas)
   # pil_image.show()
    
    if(cv2.waitKey(1)&0xff==ord('q')):
        break
video_capture.release()
cv2.destroyAllWindows()

