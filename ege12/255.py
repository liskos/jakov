def f(s):
    while "<>" not in s:
        s = s.replace(">1","3>",1)
        s = s.replace(">2","2>",1)
        s = s.replace(">3","1>",1)
        s = s.replace("3<","1>",1)
        s = s.replace("2<","<3",1)
        s = s.replace("1<","<2",1)
    return s


s = ">" + "1" * 20 + "2" * 15 + "3" * 40 + "<"
