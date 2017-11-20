
CURR_LANG = "rs" # "rs" or "en"

rsdict = { 
    "prompt" : """
Odaberite opciju:
1. Gašenje svih računara u učionici
2. Provera da li su računari uključeni
3. Izvršavanje zadate komande na svim računarima
4. Gašenje računara za katedrom (lokalno)
5. VNC remote pogled računara
------------------------------------------
0. Izlaz
    """, 
    "offin2" : "Računar će se ugasiti za 2 sekunde.",
    "noopchosen" : "Nije odabrana opcija",
    "checking" : "Provera {}...",
    "longrun" : "Za komande koje dugo traju i ne treba output (npr. instalacija paketa)\nkoristite sintaksu: 'nohup [komanda] >/dev/null 2>&1 &'",
    "inputcomm" : "Unesite komandu: ",
    "executing" : "Izvršavam '{}' na '{}'... ",
    "finished" : "Završeno.",
    "off" : "Timeout! Računar ugašen?",
    "vncuser" : "Unesite korisnicko ime koji trenutni korisnik koristi (npr. rm-user): ",
    "vnchost" : "Unesite racunar (npr. rc3-1): ",
    "vncconnected" : "Pokusaj pokretanja VNC servera na portu 5566 uspešan!",
    "vncenter" : "Pritisnite enter za konekciju.",
    "willturnoff" : "Ovo će ugasiti sve računare u učionici.", 
    "turningoff" : "Gašenje {}... "
}

endict = { 
    "prompt" : """
Choose option:
1. Turn off all the workstations
2. Check which workstations are on
3. Execute a command on all workstations
4. Turn off local machine
5. VNC view
------------------------------------------
0. Exit
    """, 
    "offin2" : "Computer will turn off in 2 seconds",
    "noopchosen" : "Nothing chosen",
    "checking" : "Checking {}...",
    "longrun" : "For long running commands where output is not important (eg. package installation)\nuse syntax: 'nohup [command] >/dev/null 2>&1 &'",
    "inputcomm" : "Command: ",
    "executing" : "Executing '{}' na '{}'... ",
    "finished" : "Finished.",
    "off" : "Timeout! Workstation off?",
    "vncuser" : "Enter current used username (eg. rm-user): ",
    "vnchost" : "Enter hostname (eg. rc3-1): ",
    "vncconnected" : "Sucessfully started VNC server on port 5566!",
    "vncenter" : "Press enter to connect.",
    "willturnoff" : "This will power off all the workstations.", 
    "turningoff" : "Powering off {}... "
}

def translate(key):
    if CURR_LANG == "rs":
        if key in rsdict:
            return rsdict[key]

    if CURR_LANG == "en":
        if key in endict:
            return endict[key]
    
    return "ERROR NO PHRASE TO TRANSLATE: " + key

