import ipaddress
k = 0
net = ipaddress.ip_network("158.132.161.128/255.255.255.128",0)
for ip in net:
    if ip.__format__("b")[-2] == "0" and ip.__format__("b")[-1] == "0":
        k+=1
print(k)