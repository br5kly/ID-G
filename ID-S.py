import platform
import os
bit = platform.architecture()[0]
if bit == "64bit":
   os.system('cd B64 && python ID-S.py')
if bit == "32bit":
    os.system('cd B32 && python ID-S.py')
