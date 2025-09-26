class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() # first step in order for our theorom to work
        count = 0
        n = len(nums)
        # step 2: loop from the end for the largest side c
        for i in range(n - 1, 1, -1):
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