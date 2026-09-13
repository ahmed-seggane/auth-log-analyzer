lignes = [
    "Sep  7 03:11:09 srv-web-01 sshd[4131]: Failed password for root from 203.0.113.42 port 51502 ssh2",
    "Sep  7 03:11:02 srv-web-01 sshd[4127]: Failed password for invalid user admin from 203.0.113.42 port 51422 ssh2",
    "Sep  7 06:02:17 srv-web-01 sshd[5021]: Accepted password for ahmed from 192.0.2.15 port 49802 ssh2",
]

tout = [ ]

for ligne in lignes :

    tout.extend(ligne.split())
    

list_ip  = []
list_users = []
compteur = {}  

for i, mot in enumerate(tout) :
    if mot == "from" :
        list_ip.append(tout[i+1])
        list_users.append(tout[i-1])
        

#print(list_ip,list_users)


for ip in list_ip :
    compteur[ip] = compteur.get(ip, 0) + 1

#print(compteur)

bigger = 0 
bigger_ip = ""


for ip, occurence in compteur.items():
    if occurence>bigger :
        bigger = occurence 
        bigger_ip = ip


print(bigger, bigger_ip)        