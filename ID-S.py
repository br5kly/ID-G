import platform
import os
bit = platform.architecture()[0]
if bit == "64bit":
   os.system('cd 64B && python ID-S.py')
if bit == "32bit":
    os.system('cd 32B && python ID-S.py')
