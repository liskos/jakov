a = []
for s1 in "12345678":
    for s2 in "012345678":
        for s3 in "012345678":
            for s4 in "012345678":
                for s5 in "012345678":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("3") == 1 and ("35" not in s) and ("36" not in s) and ("37" not in s) and ("38" not in s) and ("53" not in s) and ("63" not in s) and ("73" not in s) and ("83" not in s):
                        a.append(s)
print(len(a))