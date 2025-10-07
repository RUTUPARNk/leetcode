class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        lake_full = {}
        dry_days = []

        for i in range(n):
            if rains[i] > 0:
                ans[i] = -1
                lake = rains[i]
                if lake in lake_full:
                    found = False
                    for j, day in enumerate(dry_days):
                        if day > lake_full[lake]:
                            ans[day] = lake
                            dry_days.pop(j)
                            found = True
                            break
                    if not found:
                        return []  # no way to prevent flood
                lake_full[lake] = i
            else:
                dry_days.append(i)

        return ans
