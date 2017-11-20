#!/usr/bin/python3
import os
import subprocess

hostnames = {
    "50:65:f3:1c:ad:95" : "nmhp",
    "d8:cb:8a:9d:98:a6" : "rc3-katedra",
    "d8:cb:8a:9d:97:de" : "rc3-1",
    "d8:cb:8a:9d:97:d9" : "rc3-2",
    "d8:cb:8a:9d:97:d3" : "rc3-3",
    "d8:cb:8a:99:fa:54" : "rc3-4",
    "d8:cb:8a:9d:97:cf" : "rc3-5",
    "d8:cb:8a:9d:97:d8" : "rc3-6",
    "d8:cb:8a:99:fa:52" : "rc3-7",
    "d8:cb:8a:9d:98:c0" : "rc3-8",
    "d8:cb:8a:9d:97:dd" : "rc3-9",
    "d8:cb:8a:9d:97:d4" : "rc3-10",
    "d8:cb:8a:9d:97:e8" : "rc3-11",
    "d8:cb:8a:9d:97:d7" : "rc3-12",
    "d8:cb:8a:99:fb:4e" : "rc3-13",
    "d8:cb:8a:99:fa:76" : "rc3-14",
    "d8:cb:8a:9d:97:d5" : "rc3-15",
    "d8:cb:8a:9d:98:0f" : "rc3-16",
    "d8:cb:8a:9d:97:f0" : "rc3-17",
    "d8:cb:8a:9d:98:5f" : "rc3-18",
    "d8:cb:8a:9d:97:e4" : "rc3-19",
    "d8:cb:8a:99:fa:19" : "rc3-20",
    "d8:cb:8a:9d:98:43" : "rc3-21",
    "d8:cb:8a:9d:97:f8" : "rc3-22",
    "d8:cb:8a:9d:97:fe" : "rc3-23",
    "d8:cb:8a:9d:97:cc" : "rc3-24"
}

def get_hostname():
    return str.rstrip(subprocess.check_output("hostname", shell=True).decode("utf-8"))
    

def get_hwaddr():
    paths = ["/sys/class/net/enp3s0/address", "/sys/class/net/eno1/address", "/sys/class/net/eno0/address"]
    for path in paths:
        if os.path.exists(path):
            host = subprocess.check_output("cat {}".format(path), shell=True)
            host = str.rstrip(host.decode("utf-8"))
            return host
    return "not found" 
    

def set_hostname(hostname):
    command = 'hostnamectl set-hostname --static "{}"'.format(hostname)
    print ("+exec: {}".format(command))
    os.system(command)    

mac = get_hwaddr()
host = get_hostname()

for k,v in hostnames.items():
    if mac == k:
        if host != v:
            set_hostname(v)
            print("Sucessfully set hostname {} for {}".format(v, k))
        else:
            print("Hostname already set")


