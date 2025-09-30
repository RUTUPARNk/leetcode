class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity: int) -> bool:
            days_needed = 1
            current_load = 0
            for weight in weights:
                if current_load + weight <= capacity:
                    current_load += weight
                else:
                    days_needed += 1
                    current_load = weight
            return days_needed <= days
        low = max(weights)
        high = sum(weights)
        min_capacity = high # for worst case maximum
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                min_capacity = mid
                high = mid - 1
            else:
                low = mid + 1
        return min_capacity