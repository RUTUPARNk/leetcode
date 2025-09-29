class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def dp(i, j):
            if j - i < 2:
                return 0
            ans = float('inf')
            for k in range(i+1, j):
                score = values[i] * values[k] * values[j]
                total = score + dp(i, k) + dp(k, j)
                ans = min(ans, total)
            return ans
        return dp(0, n-1)