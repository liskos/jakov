s = open("")
w = s.split("Y")
m = 0
for i in range(len(w)-):
    a = "Y".join(w[i:i+151])
    m = max(len(a),m)
print(m)