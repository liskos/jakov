import ipaddress

for x in range(256):
    try:
        net = ipaddress.ip_network(f"172.16.168.0/255.255.255.{x}",0)
    except ValueError:
        pass

    count = 0
    for ip in net:

        if ip.__format__("b").count("0") % 7 == 0:
            count += 1

    if count == 35:
        print(x)
        break
