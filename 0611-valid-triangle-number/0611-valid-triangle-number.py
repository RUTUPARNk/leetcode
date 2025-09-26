class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() # first step in order for our theorom to work
        count = 0
        n = len(nums)
        # step 2: loop from the end for the largest side c
        for i in range(n - 1, 1, -1):
            # check 1: the worst-case shortcut
            # if the two largest remaining sides can't form a triangle, then no other sides can either. we can skip the rest of the inner loop
            if nums[i - 2] + nums[i-1] <= nums[i]:
                continue
            # The best-case shortcut, if the two smallest numbers can form a triangle with nums[i], then every pair in this range will. we can calculate the total and stop the loop early.
            if nums[0] + nums[1] > nums[i]:
                # this part is bit trick and needs a more complex formula, but the idea is to calculate all combinations from 0 to i. the core algorithm handles this more simply without this check.
                pass
                
            j = 0 # pointer for the smallest side a
            k = i - 1 # pointer for the second side b
            # step 3: two pointer loop
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    # if condition is met, all numbers between j and k will also satisfy the condition
                    count += (k - j)
                    k -= 1 # try to find more triangles with a smaller b 
                else:
                    # if the sum is too small, increase the smallest side with a
                    j += 1
        return count