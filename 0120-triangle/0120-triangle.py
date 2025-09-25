class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # this is our temp list to store min path sums, initializing it with the last row of the triangle, meaning going with bottom-up approach
        dp = triangle[-1]

        # iterating from the second to last row up to the top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
        