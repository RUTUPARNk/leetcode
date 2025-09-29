class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # initialize result array
        result = [0] * n
        stack = []

        for i in range(n):
            current_temp = temperatures[i]
            while stack and current_temp > temperatures[stack[-1]]:
                j = stack.pop()
                wait_time = i - j
                result[j] = wait_time
            stack.append(i)
        return result