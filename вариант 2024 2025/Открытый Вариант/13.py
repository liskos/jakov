import ipaddress

net = ipaddress.ip_network("98.81.154.195/255.252.0.0",0)

for ip in net.hosts():
    print(ip)

