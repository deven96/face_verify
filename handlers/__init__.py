import os
import sys

from os.path import dirname

sys.path.append(dirname(os.path.realpath(__file__)))

from verify import Verifier
from upload import Uploader