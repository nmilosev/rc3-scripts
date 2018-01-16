#!/usr/bin/python3
import ssh
from term import bcolors
import os
import time
import translate as t

"""
This Python module executes a given command on all machines.
"""

def cmd(password):
    
    print(t.translate("longrun"))
    
    command = input(t.translate("inputcomm"))
    
    cmdrun(command, password)

def cmdrun(command, password):
    for host in ssh.gethostnames():
        print(t.translate("executing").format(command, host), end="")
        try:
            output = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))
            print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
            print("Output: {}".format(output[31:]))
        except:
            print(bcolors.FAIL + t.translate("off") + bcolors.ENDC)
        
    print(t.translate("finished"))
    
def vnc(password):
    
    host = "rc3-" + input(t.translate("vnchost")).replace("rc3-", "")
    print(t.translate("loggedin"))
    
    who = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, "'who | grep -v rc3-admin'"))[33:]
    
    if len(who.split("\n")) > 1:
        print(who)
        user = input(t.translate("vncuser"))

        tty = ":0"
        for str in who.split("\n"):
            if user in str:
                tty = str.split()[4].strip().replace("(", "").replace(")", "")
                break
    else:
        user = who.split()[0].strip()
        tty = who.split()[4].strip().replace("(", "").replace(")", "")

    vncconnect(tty, user, host, password)

    print(t.translate("finished"))
 
def vncone(password):
    vncall(password, [ input(t.translate("vnchost")) ], True)

def vncall(password, hosts, skipRemmina):
    user = input(t.translate("vncuser"))
    
    for host in hosts:
        print("VNC start: '{}:5566'... ".format(host), end="")
        try:
            who = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, "'who | grep -v rc3-admin'"))[33:]

            tty = ":0"
            for str in who.split("\n"):
                if user in str:
                    tty = str.split()[4].strip().replace("(", "").replace(")", "")
                    break

            vncstart(tty, user, host, password)

            print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + t.translate("off") + bcolors.ENDC)
    if not skipRemmina: 
        print("rc3-admin login:")
        print(t.translate("loginpromptremind"))
        os.system("su - rc3-admin -c 'remmina'")

def vncstart(tty, user, host, password):
    command = 'nohup x11vnc -noxdamage -display {} -rfbport 5566 -auth /run/user/`id -u {}`/gdm/Xauthority &'.format(tty, user)
    _ = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))

def vncconnect(tty, user, host, password):
    command = 'nohup x11vnc -noxdamage -display {} -rfbport 5566 -auth /run/user/`id -u {}`/gdm/Xauthority &'.format(tty, user)
    _ = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))
    time.sleep(1)
    os.system("nohup vncviewer -ViewOnly {}:5566 >/dev/null 2>&1 &".format(host))

if __name__ == "__main__":
    cmd(ssh.getpassword())
