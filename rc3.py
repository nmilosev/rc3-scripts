#!/usr/bin/python3
import rc3check, rc3cmd, rc3off, ssh, os

"""
Glavna aplikacija
"""

def main():
    os.system("clear")
    
    password = ssh.getpassword()

    while True:
        os.system("clear")
        print("Odaberite opciju:")
        print("1. Gašenje svih računara u učionici")
        print("2. Provera da li su računari uključeni")
        print("3. Izvršavanje zadate komande na svim računarima")
        print("4. Gašenje računara za katedrom (lokalno)")
        print("------------------------------------------")
        print("0. Izlaz")

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
            print("Računar će se ugasiti za 3 sekunde.")
            os.system(rc3off.off_command)
            break
        else:
            print("Niste odabrali opciju.")

        #wait:
        input()

if __name__ == "__main__":
    main()