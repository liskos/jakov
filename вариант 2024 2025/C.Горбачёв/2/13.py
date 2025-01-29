import ipaddress
k = 0
net = ipaddress.ip_network("82.230.106.168/255.255.255.240",0)
for ip in net:
    if (ip.__format__("b")[8:15]).count("1") % 3 == 0 and (ip.__format__("b")[16:24]).count("1") % 3 == 0:
        k+=1


print(k)