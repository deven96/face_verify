import time
from handlers import Verifier, Uploader

start = time.time()
uploader = Uploader("Any Name")
print("Uploader Class works, initialized in {time.time()-start}")
start = time.time()
ver = Verifier()
print("Verifier Class works, initialized in {time.time()-start}")
