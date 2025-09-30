class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums)- 1):
                sum_mod_10 = (nums[i] + nums[i + 1]) % 10
                new_nums.append(sum_mod_10)
            nums = new_nums
        return nums[0]