#!/usr/bin/python3
import ssh
import getpass
from term import bcolors

"""
Ovaj Python modul proverava da li su računari uključeni, za
hostname-ove od rc3-1 do rc3-24. Pristupa preko SSH kao jedini 
korisnik kojem je to dozvoljeno rc3-admin.
"""

def check(password):
    # komanda: - uptime uvek radi pa mozemo nju da koristimo za proveru
    command = "uptime"

    for host in ssh.gethostnames():
        print("Provera {}... ".format(host), end="")
        try:
            ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))
            print(bcolors.OKGREEN + "ON" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "OFF" + bcolors.ENDC)
        
    print("--------")      


if __name__ == "__main__":
    check(ssh.getpassword())
