import ipaddress
k = 0
net = ipaddress.ip_network("111.194.0.0/255.254.0.0",0)

for ip in net.hosts():
    if (ip.__format__("b").count("1") - ip.__format__("b").count("0")) % 2 == 0:
        k+=1


print(k)