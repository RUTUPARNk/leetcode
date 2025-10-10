class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
            n = len(energy)
            dp = [0] * n
            for i in range(n - 1, -1, -1):
                if i + k < n:
                    dp[i] = energy[i] + dp[i + k]
                else:
                    dp[i] = energy[i]
            result = dp[0]
            for i in range(1, n):
                if dp[i] > result:
                    result = dp[i]
            return result