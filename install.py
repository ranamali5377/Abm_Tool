#/usr/bin/python2
import os
import re
import time
import platform
os.system("pip2 install requests bs4")

try:
     import bs4
except IOError:
     os.system("pip2 install requests bs4")
   
try:
     import requests
except IOError:
     os.system("pip2 install requests")

bit = platform.architecture()[0]
if bit == '64bit':
    from tool64 import main_abm
    main_abm()
elif bit == '32bit':
    from inittool32 import main_abm
    main_abm()     
