s = open("24data/24-268.txt").read()
import re
import string
pattern = r"((([13579BDFHJLNPRT][02468ACEGIKMOQS])+([13579BDFHJLNPRT]?))|([2468ACEGIKMOQS]([13579BDFHJLNPRT][02468ACEGIKMOQS])*([13579BDFHJLNPRT]?)))"
pattern2 = rf"[^0123456789ABCDEFGHIJKLMNOPQRST]{pattern}[^0123456789ABCDEFGHIJKLMNOPQRST]"
b = [len(x.group()[1:-1]) for x in re.finditer(pattern2,s)]
print(max(b))
b = [x.group()[1:-1] for x in re.finditer(pattern2,s)]
print(*[x for x in b if len(x)==10])