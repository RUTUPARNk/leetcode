class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            stri = str(num)
            if len(stri) % 2 == 0:
                count += 1
        return count