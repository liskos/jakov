import ipaddress

net = ipaddress.ip_network("142.36.195.251/255.255.255.192",0)

for ip in net.hosts():
    print(ip)
