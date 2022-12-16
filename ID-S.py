import platform
import os
try:
    import requests
except ModuleNotFoundError:
    os.system("python setup.py")
bit = platform.architecture()[0]
if bit == "64bit":
   os.system('cd as-main && python s.py')
if bit == "32bit":
    os.system('cd as-main && cd tests-main && python ID-S.py')
