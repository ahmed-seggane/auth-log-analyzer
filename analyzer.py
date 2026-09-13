from collections import Counter

lignes = [
    "Sep  7 03:11:02 srv-web-01 sshd[4127]: Failed password for invalid user admin from 203.0.113.42 port 51422 ssh2",
    "Sep  7 03:11:04 srv-web-01 sshd[4127]: Failed password for invalid user admin from 203.0.113.42 port 51436 ssh2",
    "Sep  7 03:11:09 srv-web-01 sshd[4131]: Failed password for root from 203.0.113.42 port 51502 ssh2",
    "Sep  7 03:12:44 srv-web-01 sshd[4140]: Failed password for root from 198.51.100.7 port 40112 ssh2",
    "Sep  7 03:14:01 srv-web-01 sshd[4155]: Failed password for invalid user test from 203.0.113.42 port 51688 ssh2",
    "Sep  7 06:02:17 srv-web-01 sshd[5021]: Accepted password for ahmed from 192.0.2.15 port 49802 ssh2",
    "Sep  7 06:44:53 srv-web-01 sshd[5099]: Failed password for ahmed from 192.0.2.15 port 49930 ssh2",
    "Sep  7 06:44:58 srv-web-01 sshd[5099]: Accepted password for ahmed from 192.0.2.15 port 49930 ssh2",
    "Sep  7 09:30:12 srv-web-01 sshd[6210]: Failed password for invalid user postgres from 198.51.100.7 port 40560 ssh2",
    "Sep  7 09:30:15 srv-web-01 sshd[6210]: Failed password for invalid user postgres from 198.51.100.7 port 40574 ssh2",
    "Sep  7 11:58:40 srv-web-01 sshd[7002]: Accepted publickey for ahmed from 192.0.2.15 port 50044 ssh2",
    "Sep  7 23:47:31 srv-web-01 sshd[9310]: Failed password for root from 203.0.113.42 port 52110 ssh2",
]

tout = []
for ligne in lignes:
    tout.extend(ligne.split())

list_ip = []
list_users = []
list_error = []
for i, mot in enumerate(tout):
    if mot == "from":
        list_ip.append(tout[i + 1])
        list_users.append(tout[i - 1])
    elif mot in ("Accepted", "Failed"):
        list_error.append(mot)

compteur = Counter(list_ip)

print(compteur)
print(compteur.most_common(1))
print(compteur.most_common(3))

print(Counter(list_error))