class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * 20
        dp[0] = dp[1] = 1
        dp[2] = 2
        if n < 3: return dp[n]

        for i in range(3, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]

if __name__ == '__main__':
    print(Solution().numTrees(3))