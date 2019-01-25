"""@desc 
		Verify image against database

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2019-01-25 04:24:53
 		@modify date 2019-01-25 04:24:53

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


class Verifier(object):
    """ Verifies against photos in database

        Methods:
            run
            stop
            
    """
    def __init__(self):
        self.camera = None
        self.known_face_dict = dict()
        # always process db
        self._process_database()
    
    def run(self):
        """ starts the verifier

        """
        face_locations = []
        face_names = []
        face_encodings = []
        process_this_frame = True
        cv2.namedWindow(consts.VERIFY_WINDOW)
        # TODO : video capture source should be handled by camera.py and /
        #        not default 0(webcam)
        self.camera = cv2.VideoCapture(0)
        while self.camera.isOpened():
            _, frame = self.camera.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings= face_recognition.face_encodings(rgb_small_frame, face_locations)
                known_face_encodings = list(self.known_face_dict.values())
                known_face_names = list(self.known_face_dict.keys())

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    # increase similarity index from 0.6 to 0.5 to reduce false positives
                    distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                    name = "Unknown"
                    print(f"Distance: {face_recognition.face_distance(known_face_encodings, face_encoding)}")
                    # If highest element in distance higher than threshold , use the first index.
                    if max(distance) > consts.THRESHOLD:
                        highest_index = distance.index(max(distance))
                        print(highest_index)
                        name = known_face_names[highest_index]
                    face_names.append(name)

            process_this_frame = not process_this_frame
            self._label_frame(face_locations, face_names, frame)


            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.stop()

    def stop(self):
        """ stops the uploader
        """
        self.camera.release()
        cv2.destroyAllWindows()

    def _label_frame(self, face_locations, face_names, frame):
        """ puts bounding box on image, writes the name
            and displays the image

        :param face_locations: (top, right, bottom, left) coordinates of locations
        :type face_locations: list
        :param face_names: names of those identified in each location
        :type face_names: list
        :param frame: video frame currently analysed
        :type frame: `numpy.ndarray`
        """
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow(consts.VERIFY_WINDOW, frame)
        

    def _process_database(self):
        """ Processes database
        """
        image_names = consts.IMAGES_IN_DATABASE
        # get human readable name using image name
        names = [self._readable_name(i) for i in image_names]
        # absolute location of every image stored as a list
        locations = [os.path.join(consts.DATABASE_DIR, i) for i in image_names]
        images = [face_recognition.load_image_file(i) for i in locations]
        # use face_location to try precompute known_face_locations
        encodings = [face_recognition.face_encodings(i, 
                    # face_location api uses the same engine that was used to 
                    #  detect a face for upload
                    known_face_locations=face_recognition.face_locations(
                            i,
                            number_of_times_to_upsample=0,
                            model="cnn")
                            )[0]
                    for i in images]
        self.known_face_dict = dict(zip(names, encodings))

    def _readable_name(self, name):
        """ gets the name from a single image_name

        :param name: underscore separated name
        :type name: str
        :rtype: str
        """
        if name.endswith(".jpg"):
            name = name[:-4]
            return name.replace("_", " ")
        else:
            raise Exception("Image does not end with .jpg")

# if __name__=="__main__":
#     verifier = Verifier()
#     verifier.run()