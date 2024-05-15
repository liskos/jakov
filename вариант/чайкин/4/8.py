k = 0
for s1 in "123456789ab":
    for s2 in "0123456789ab":
        for s3 in "0123456789ab":
            for s4 in "0123456789ab":
                for s5 in "0123456789ab":
                    for s6 in "0123456789ab":
                        for s7 in "0123456789ab":
                            for s8 in "0123456789ab":
                                s = s1+s2+s3+s4+s5+s6+s7+s8
                                if (sum([s.count(i) for i in "2357b"]) >= 2) and (int(s1, 12) % 2 != int(s8, 12) % 2):
                                    k += 1
print(k)