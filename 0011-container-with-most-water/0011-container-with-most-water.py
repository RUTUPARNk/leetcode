class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(current_area, max_area)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area