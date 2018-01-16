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
        elif i == 6:
            rc3off.off(password)
            print(t.translate("offin2"))
            os.system(rc3off.off_command)
        elif i == 7:
            rc3cmd.vncall(password, ssh.gethostnames(), False)
        elif i == 8:
            rc3cmd.vncone(password)
        else:
            print(t.translate("noopchosen"))

        input()

if __name__ == "__main__":
    main()
