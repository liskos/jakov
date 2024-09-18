a = set()
for s1 in "просто":
    for s2 in "просто":
        for s3 in "просто":
            for s4 in "просто":
                for s5 in "просто":
                    for s6 in "просто":
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        if s.count('п') == 1 and s.count('р') == 1 and s.count('о') == 2 and s.count('т') == 1 and 'оо' not in s:
                            a.add(s)
print(len(a))
