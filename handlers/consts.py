"""@desc 
		Constants

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2019-01-24 22:27:16
 		@modify date 2019-01-24 22:27:16

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """
import os

from os.path import dirname

HANDLER_DIR = dirname(os.path.realpath(__file__))
ROOT_DIR = dirname(HANDLER_DIR)


# image variables
PADDING = 50
THRESHOLD = 0.4

# database 
DATABASE_DIR = os.path.join(ROOT_DIR, "database")
IMAGES_IN_DATABASE = [i for i in os.listdir(DATABASE_DIR) if not str(i).startswith(".")]

# window names
UPLOADER_WINDOW = "Upload Picture to database"
VERIFY_WINDOW = "Verify Person is in database"