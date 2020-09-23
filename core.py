# Shell & Core for IonOS 1.0.
# Written in vanilla Python 3.

import os
import sys

def kernel():
    def kill(ptk):
      if ptk == None or == "" or == 0: return 0
      elif ptk == 1 or == 0: print("Can't kill main process!")
      elif ptk in range(9999999999): os.kill(ptk)
      else: print("Error killing process.")
    def memoryload():
      # Fill this later on
