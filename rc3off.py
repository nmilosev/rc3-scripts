#!/usr/bin/python3
import ssh
import getpass
from term import bcolors

"""
Ovaj Python modul gasi sve računare sa hostname-ovima 
od rc3-1 do rc3-24. Pristupa preko SSH kao jedini korisnik
kojem je to dozvoljeno rc3-admin.
"""

# komanda:
# mora sleep 3 da sačeka 3 sekunde, kako bi se otkačio ssh
off_command = "nohup sleep 3 && systemctl poweroff -i >/dev/null 2>&1 &"

def off(password):
    print("Ovo će ugasiti sve računare u učionici.")
       
    for host in ssh.gethostnames():
        print("Gašenje {}... ".format(host), end="")
        try:
            ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, off_command))
            print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "Timeout! Računar već ugašen?" + bcolors.ENDC)
        
    print("Završeno. Projektor se gasi ručno. :)")      

if __name__ == "__main__":
    off(ssh.getpassword())
