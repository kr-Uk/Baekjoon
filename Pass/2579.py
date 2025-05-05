dp = [0] * 301
n = int(input())
score = [0]

for _ in range(n):
    score.append(int(input()))

if n >= 1:
    dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]
if n >= 3:
    dp[3] = max(score[1] + score[3], score[2] + score[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + score[i] + score[i-1], dp[i-2] + score[i])
    
print(dp[n])