s=open("24data/24-1.txt").read()
i = 1
while "C"*i in s:
    i += 1
print(i-1)




# s=open("24data/24-1.txt").read()
#
# for i in range(1,len(s)):
#     if "C"*i in s:
#         print(i)
#     else:
#         break
