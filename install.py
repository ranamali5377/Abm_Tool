#/usr/bin/python2
import os
import re
import time
import platform

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
    os.system("uname -om")
    print("")
    print("Welcome to abm-tool platform ").center(50)
    knock = raw_input("\tInstall abm_tool with platform (32bit/64bit) ")
    if knock =="32bit":
        os.system("cd cool && python2 cool")
    if knock =="64bit":
        os.system("cd tool && python2 tool")
    else:
        print("")
        print("unknow aarch device or invalid system").center(50)
        print("")
        time.sleep(1)
        main()
        
if __name__ == '__main__':
    main()
