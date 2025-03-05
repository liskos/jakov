import ipaddress
k  = 0
net = ipaddress.ip_network("68.30.20.77/192.0.0.0",0)
for ip in net.hosts():
    if bin(int(ip)).count("1") == 10:  # Переводим IP в бинарный вид и считаем единицы
        k += 1

print(k)
