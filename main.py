"""@desc 
		Main handler(command line)
        TODO: change handler to actual GUI

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2019-01-25 00:51:13
 		@modify date 2019-01-25 00:51:13

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """
"""@desc 
		[description]

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2019-01-25 00:51:11
 		@modify date 2019-01-25 00:51:11

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """
import argparse
import time

from handlers import Verifier, Uploader

parser = argparse.ArgumentParser(prog="Facial Verification System")
# two different parsers for the program , one for upload and one for verify
subparsers = parser.add_subparsers(help='sub-command help', dest="subparser_name")

upload_parser = subparsers.add_parser('upload', help='upload help')
upload_parser.add_argument("--name",
				type=str,
                required=True,
				help="Name to give image e.g 'Sherlock Holmes'")

verify_parser = subparsers.add_parser('verify', help="verify help")

args = parser.parse_args()

if args.subparser_name == "upload":
    strt = time.time()
    uploader = Uploader(name=args.name)
    print(f"Initialized uploader in {time.time()-strt}")
    uploader.run()
else:
    strt = time.time()
    verifier = Verifier()
    print(f"Initialized verifier in {time.time()-strt}")
    verifier.run()