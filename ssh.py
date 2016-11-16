import getpass
from netmiko import ConnectHandler

"""
SSH modul koji koristi netmiko biblioteku kao osnovu.
"""

def run(hostname, port, username, password, command):
    """
    Izvršava komandu (command) na hostname:port sa zadatim username-om i password-om.

    Vraća string, ono što je komanda ispisala.
    """
    node = {
        'device_type': 'linux',
        'ip':   hostname,
        'username': username,
        'password': password,
        'port' : port,          # optional, defaults to 22
        'verbose': False,       # optional, defaults to False
    }

    connection = ConnectHandler(**node)

    output = connection.send_command(command)

    connection.disconnect()
    
    return output

# kao root (jedino rc3-admin ima sudo, password ne čuvamo u fajlu već unosi korisnik):
# prvi razmak znaci da se ne cuva password u history-ju
def suwrap(password, command):
    return " sudo -S <<< \"{}\" su -c '{}'".format(password, command)

def gethostnames():
    return ["rc3-{}".format(i) for i in range(1, 24 + 1)]

def getpassword():
    return getpass.getpass("rc3-admin password: \n")