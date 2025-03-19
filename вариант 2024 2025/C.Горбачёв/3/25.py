import fnmatch

for i in range(25641,10**11,25641):
    if fnmatch.fnmatch("4?78*82?1",str(i)):
        if not fnmatch.fnmatch("4?78?82?1",str(i)):
            print(i,i//3489)





#import re
# pattern_main = r"4\d78\d*82\d1"  # \d* — это любое количество цифр (включая 0)
# pattern_bad = r"4\d78\d82\d1"     # \d — ровно одна цифра вместо *
#
# for i in range(25641, 10**11, 25641):
#     s = str(i)
#     if re.fullmatch(pattern_main, s):
#         if not re.fullmatch(pattern_bad, s):
#             print(i, i // 3489)
