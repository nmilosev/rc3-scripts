#!/usr/bin/python3
import ssh
import getpass
import translate as t
from term import bcolors

"""
This module checks if all the machines are on from rc3-1 to rc3-24. 
It uses SSH and uptime command. If anything is returned we know host
is up.
"""

def check(password):
    command = "uptime"

    for host in ssh.gethostnames():
        
        print(t.translate("checking").format(host), end="")
        try:
            ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))
            print(bcolors.OKGREEN + "ON" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "OFF" + bcolors.ENDC)
        
    print("--------")      


if __name__ == "__main__":
    check(ssh.getpassword())
