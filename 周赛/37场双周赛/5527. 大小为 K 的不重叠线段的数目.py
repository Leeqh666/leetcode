class Solution:
    def numberOfSets(self, n: int, ki: int) -> int:
        mod=10**9+7
        dp=[[0]*(ki+1) for i in range(n)]
        for i in range(n):
            dp[i][0]=1
        for p in reversed(range(n-1)):
            for k in range(1,ki+1):
                if p==n-2:
                    dp[p][k]=(dp[p+1][k-1]+dp[p+1][k])%mod
                else:
                    dp[p][k]=(dp[p+1][k-1]+2*dp[p+1][k]-dp[p+2][k])%mod
        return dp[0][ki]%mod