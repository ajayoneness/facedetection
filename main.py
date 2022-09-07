import cv2
import numpy as np
import face_recognition



my_image = face_recognition.load_image_file('image/codeaj.jpg')
my_image = cv2.cvtColor(my_image,cv2.COLOR_BGR2RGB)

facelocation = face_recognition.face_locations(my_image)[0]
encodeimg = face_recognition.face_encodings(my_image)[0]
cv2.rectangle(my_image,(facelocation[3],facelocation[0]),(facelocation[1],facelocation[2]),(255,0,255))


cap = cv2.VideoCapture(0)

# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

while True:
    sucess,img = cap.read()

    try:
        facelocation = face_recognition.face_locations(img)[0]
        encodeimg = face_recognition.face_encodings(img)[0]
        print(facelocation)
        print(encodeimg)
        cv2.rectangle(img,(facelocation[3],facelocation[0]),(facelocation[1],facelocation[2]),(255,0,255))
    except:
        print('you are not in the camera')

    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# test_image = face_recognition.load_image_file('image/test.jpg')
# test_image = cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB)
#
#
#
#
#
# facelocationtest = face_recognition.face_locations(test_image)[0]
# encodeimgtest = face_recognition.face_encodings(test_image)[0]
# cv2.rectangle(test_image,(facelocation[3],facelocation[0]),(facelocation[1],facelocation[2]),(0,5,255))
#
#
# result =  face_recognition.compare_faces([encodeimg],encodeimgtest)
#
# facedis = face_recognition.face_distance([encodeimg],encodeimgtest)
# cv2.putText(test_image,f"{result} {round(facedis[0],2)}",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
#
# print(result)
# print(facedis)
#
#
# cv2.imshow("codeaj-1",my_image)
# cv2.imshow("codeaj-2",test_image)
#
# cv2.waitKey(0)