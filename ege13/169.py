import ipaddress

def f(a):
     return len(set(a)) == 3

net = ipaddress.ip_network("117.32.0.0/255.224.0.0",0)
b = set()
for ip in net.hosts():
    if f([ip.packed[0],ip.packed[1],ip.packed[2],ip.packed[3]]):
        b.add(ip)

print(len(b))

