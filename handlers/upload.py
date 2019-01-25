"""@desc 
		Upload photo to the database


 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2019-01-24 22:28:43
 		@modify date 2019-01-24 22:28:43

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """
import os
import cv2
import dlib
import face_recognition
import numpy as np
import consts


class Uploader(object):
    """ Handler for uploading images to the database.
        Triggers the camera input and then uses opencv's to detect a face
        in the image for upload

        :param name: name of the person in format "Firstname Lastname"
        :type name: str
            
    """
    def __init__(self, name):
        self.name = name
        self.filename = self.name.replace(" ", "_") + ".jpg"
        self.detector = dlib.get_frontal_face_detector()
        self.ready_to_detect_face = True
        self.camera = None
    
    def run(self):
        """ starts the uploader and shows bounding boxes
            for a detected face

        """

        cv2.namedWindow(consts.UPLOADER_WINDOW)
        # TODO : video capture source should be handled by camera.py and /
        #        not default 0(webcam)
        self.camera = cv2.VideoCapture(0)
        while self.camera.isOpened() and self.ready_to_detect_face:
            _, frame = self.camera.read()
            face_coords = self._detect_face(frame)
            # draw rectangle bounding box for every face
            for i in face_coords:
                print("found face coords")
                self._upload(frame)
                cv2.rectangle(frame,(i[0], i[1]),(i[2], i[3]),(255,0,0),2)
                print(f"Detected face: uploading as {self.name} .. exiting")
                self.ready_to_detect_face = False

            key = cv2.waitKey(100)
            cv2.imshow(consts.UPLOADER_WINDOW, frame)

            if key == 27: # exit on ESC
                break
        self.stop()

    def stop(self):
        """ stops the uploader
        """
        self.camera.release()
        cv2.destroyAllWindows()
    
    def _detect_face(self, frame):
        """ detects the face in the frame

        :param frame: single frame of the video feed
        :type frame: `np.ndarray`
        :rtype: list[tuples]
        """
        face_coords = list()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 0)
        print(rects)
        # get bounding box for every face in the frame
        for i, d in enumerate(rects):
            x1 = d.left()-consts.PADDING
            y1 = d.top()-consts.PADDING
            x2 = d.right()+consts.PADDING
            y2 = d.bottom()+consts.PADDING
            face_coords.append((x1, y1, x2, y2))
        return face_coords

    def _upload(self, frame):
        """ uploads the image to the database

        :param frame: single frame of the video feed
        :type frame: `np.ndarray`
        """
        full_image_location = os.path.join(consts.DATABASE_DIR, self.filename)
        cv2.imwrite(full_image_location, frame)


# if __name__=="__main__":
#     uploader = Uploader("Diretnan Domnan")
#     uploader.run()