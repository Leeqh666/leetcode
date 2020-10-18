from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        w=sorted(zip(ages,scores))
        n=len(w)
        dp=[0]*n
        dp[0]=w[0][1]
        for i in range(1,n):
            dp[i]=w[i][1]
            for j in range(i):
                if w[i][0]==w[j][0] or w[i][1]>=w[j][1]:
                    dp[i]=max(dp[i],w[i][1]+dp[j])
        return max(dp)
