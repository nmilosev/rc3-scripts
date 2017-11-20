#!/usr/bin/python3
import ssh
import getpass
from term import bcolors
import translate as t

"""
This python module powers off all the machines.
"""

# sleep 2 seconds for SSH to disconnect
off_command = "nohup sleep 2 && systemctl poweroff -i >/dev/null 2>&1 &"

def off(password):
    print(t.translate("willturnoff"))
       
    for host in ssh.gethostnames():
        print(t.translate("turningoff").format(host), end="")
        try:
            ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, off_command))
            print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + t.translate("off") + bcolors.ENDC)
    print(t.translate("finished"))      

if __name__ == "__main__":
    off(ssh.getpassword())
