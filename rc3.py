#!/usr/bin/python3
import rc3check, rc3cmd, rc3off, ssh, os, sys
import translate as t

"""
Main application entry point
"""

def main():

    if "-en" in sys.argv:
        t.CURR_LANG = "en"

    os.system("clear")
    
    password = ssh.getpassword()

    while True:
        os.system("clear")
        
        print(t.translate("prompt").rstrip().lstrip())

        i = int(input())

        if i == 0:
            break
        elif i == 1:
            rc3off.off(password)
        elif i == 2: 
            rc3check.check(password)
        elif i == 3: 
            rc3cmd.cmd(password)
        elif i == 4:
            print(t.translate("offin2"))
            os.system(rc3off.off_command)
            break
        elif i == 5:
            rc3cmd.vnc(password)
        else:
            print(t.translate("noopchosen"))

        input()

if __name__ == "__main__":
    main()
