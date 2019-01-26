# helper functions to be used
import os
import face_recognition
import cv2
import consts


def readable_name(name):
        """ gets the name from a single image_name

        :param name: underscore separated name
        :type name: str
        :rtype: str
        """
        cdef str cname = name
        if cname.endswith(".jpg"):
            cname = name[:-4]
            return cname.replace("_", " ")
        else:
            raise Exception("Image does not end with .jpg")


def process_database():
    """ Processes database
    """
    # declare static variables to be used
    cdef str i = ""


    image_names = consts.IMAGES_IN_DATABASE
    # get human readable name using image name
    names = [readable_name(i) for i in image_names]
    # absolute location of every image stored as a list
    locations = [os.path.join(consts.DATABASE_DIR, i) for i in image_names]
    images = [face_recognition.load_image_file(i) for i in locations]
    # use face_location to try precompute known_face_locations
    encodings = [face_recognition.face_encodings(x, 
                # face_location api uses the same engine that was used to 
                #  detect a face for upload
                known_face_locations=face_recognition.face_locations(
                        x,
                        number_of_times_to_upsample=0,
                        model="cnn")
                        )[0]
                for x in images]
    return dict(zip(names, encodings))
