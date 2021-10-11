#/usr/bin/python2
import os
import re
import time

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
    print("[1] Install Abm-Tool 32bit Platform")
    time.sleep(0.05)
    print("[2] Install Abm-Tool 64bit Platform")
    time.sleep(0.05)
    print("[0] Tool Logout")
    time.sleep(0.05)
    print('--------------------------------------------------')
    mx()
def mx():
    knock = raw_input("[!] choose input : ")
    if knock =="1":
        os.system("cd pool")
        os.system("python2 pool")
    elif knock =="2":
        os.system("cd tool && python2 tool.py")
    elif knock =="0":
        os.system("exit")
    else:
        print("")
        print("please select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
        
if __name__ == '__main__':
    main()
