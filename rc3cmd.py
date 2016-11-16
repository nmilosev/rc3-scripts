#!/usr/bin/python3
import ssh
from term import bcolors

"""
Ovaj Python modul izvršava zadatu komandu kao root na svim
hostname-ovima od rc3-1 do rc3-24. Pristupa preko SSH kao 
jedini korisnik kojem je to dozvoljeno rc3-admin.
"""

def cmd(password):
    
    print("Za komande koje dugo traju i ne treba output (npr. instalacija paketa)\nkoristite sintaksu: 'nohup [komanda] >/dev/null 2>&1 &'")
    
    # komanda:
    command = input("Unesite komandu: ")

    for host in ssh.gethostnames():
        print("Izvršavam '{}' na '{}'... ".format(command, host), end="")
        try:
            output = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))
            print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
            print("Output: {}".format(output[31:]))
        except:
            print(bcolors.FAIL + "Timeout! Računar ugašen?" + bcolors.ENDC)
        
    print("Završeno.")

if __name__ == "__main__":
    cmd(ssh.getpassword())
