#/usr/bin/python2
import os
import re
import time
import platform

try:
    import cythonize
except IOError:
    os.system("pip install cythonize")
    os.system("pip2 install cythonize")

try:
    os.mkdir("/sdcard/abm_tool")
except IOError:
    pass

def logo():
    print("""
     ___    ____  __  ___   __________  ____  __ 
    /   |  / __ )/  |/  /  /_  __/ __ \/ __ \/ / 
   / /| | / __  / /|_/ /    / / / / / / / / / /  
  / ___ |/ /_/ / /  / /    / / / /_/ / /_/ / /___
 /_/  |_/_____/_/  /_/    /_/  \____/\____/_____/
--------------------------------------------------
(~) Author  : Tech Abm
(~) Github  : https://github.com/Tech-abm
(~) Fb Page : https://facebook.com/Techabm
--------------------------------------------------                                             
""")

def main():
    os.system("clear")
    logo()
    print("")
    print("")
    print("")
    print("")
    os.system("uname -om")
    print("")
    print("Welcome to abm-tool platform").center(50)
    knock = raw_input("Install abm_tool with platform (32bit/64bit) ")
    if knock =="32bit":
        yes_aarm()
    if knock =="64bit":
        os.system("cd tool && python2 tool")
    else:
        print("")
        print("unknow aarch device or invalid system").center(50)
        print("")
        time.sleep(1)
        main()

def yes_aarm():
    os.system("clear")
    logo()
    os.system("cythonize -i tool32bit.c && rm -rf *.so")
    os.system("cythonize -i tool32bit.c")
    bit = platform.architecture()[0]
    if bit == '32bit':
        from tool import main_abm
        main_abm()

if __name__ == '__main__':
    main()
