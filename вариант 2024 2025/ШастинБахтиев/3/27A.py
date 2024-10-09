import sys,func
sys.stdin = open("27_A.txt")
n = int(input())
point = []
for _ in range(n):
    x,y,r = map(float,input().split())
    point.append([x,y,r])
star = []
for __ in range(1000):
    x,y = map(float,input().split())
    star.append([x,y])
for p in point:
    print(func.s(p,star))
# 6408 4439
# 11561 6294