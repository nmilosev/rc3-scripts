import getpass
from netmiko import ConnectHandler

"""
Main SSH module
"""

def run(hostname, port, username, password, command):
    """
    Executes command on hostname:port with given username and password.

    Returns output string.
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

def suwrap(password, command):
    return " sudo -S <<< \"{}\" su -c '{}'".format(password, command)

def gethostnames():
    return ["rc3-{}".format(i) for i in range(1, 24 + 1)]

def getpassword():
    return getpass.getpass("rc3-admin password: \n")