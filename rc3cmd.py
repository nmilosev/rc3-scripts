#!/usr/bin/python3
import ssh
from term import bcolors
import translate as t

"""
This Python module executes a given command on all machines.
"""

def cmd(password):
    
    print(t.translate("longrun"))
    
    command = input(t.translate("inputcomm"))

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
    """
    Connects via x11vnc to a given machine, to see what the user is doing.
    """    

    user = input(t.translate("vncuser"))  
    host = input(t.translate("vnchost"))

    for i in range(5):
        command = 'nohup su - {} -c "x11vnc -noxdamage -display :{} -rfbport 5566"'.format(user, i)
        _ = ssh.run(host, 22, "rc3-admin", password, ssh.suwrap(password, command))

    print(bcolors.OKGREEN + t.translate("vncconnected") + bcolors.ENDC)
    _ = input()
    os.system("vncviewer -ViewOnly {}:5566".format(host))
    print(t.translate("finished"))
    
if __name__ == "__main__":
    cmd(ssh.getpassword())
