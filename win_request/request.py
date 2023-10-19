import numpy as np
word1='horse'
word2='ros'
word1='0'+word1
word2='0'+word2
n1=len(word1)
n2=len(word2)
dp=np.zeros((n1,n2),dtype='int')
for i in range(0,n1):
    dp[i][0]=i
for j in range(0,n2):
    dp[0][j]=j

for i in range(1,n1):
    for j in range(1,n2):
        if word1[i]==word2[j]:
            mid=dp[i-1][j-1]
        else:
            mid=dp[i-1][j-1]+1
        
        dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,mid)
print(dp)
print(dp[-1][-1])