import  ipaddress


net = ipaddress.ip_network("11.92.135.56/255.224.0.0",0)

for ip in net.hosts():
    print(ip)