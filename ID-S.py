import platform
import os
bit = platform.architecture()[0]
if bit == "64bit":
   os.system('cd as-main && python s.py')
if bit == "32bit":
    os.system('cd as-main && tests-main && python ID-S.py')
