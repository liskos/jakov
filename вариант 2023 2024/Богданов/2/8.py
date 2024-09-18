a = set()
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    for s6 in "01234567":
                        for s7 in "01234567":
                            for s8 in "01234567":
                                for s9 in "01234567":
                                    for s10 in "01234567":
                                        s = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10
                                        if s.count('7') == 5 and ('17'not in s) and ('37'not in s) and ('57'not in s) and ('77'not in s)and ('71'not in s)and ('73'not in s)and ('75'not in s):
                                                a.add(s)
print(len(s))