# 그냥 sort로 해보기

import sys

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))
    
num.sort()

for i in num:
    print(i)