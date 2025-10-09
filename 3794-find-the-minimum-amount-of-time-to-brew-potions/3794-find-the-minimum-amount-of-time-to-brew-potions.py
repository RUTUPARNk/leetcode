class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        if n == 0 or m == 0:
            return 0

        # prev_pref[j] = sum_{k=0..i-1} p[k][j] for current i in loop
        prev_pref = [0] * m
        # maxd[j] will hold the maximum value of (pref_i[j] - pref_{i-1}[j+1]) across i
        maxd = [-10**18] * (m - 1)

        for i in range(n):
            # curr_pref[j] = sum_{k=0..i} p[k][j]
            curr_pref = [prev_pref[j] + skill[i] * mana[j] for j in range(m)]

            # update candidates for delta between potion j and j+1
            for j in range(m - 1):
                right = prev_pref[j + 1] if i > 0 else 0
                candidate = curr_pref[j] - right
                if candidate > maxd[j]:
                    maxd[j] = candidate

            prev_pref = curr_pref

        makespan = sum(maxd) + prev_pref[-1]  # prev_pref is now pref_{n-1}
        return makespan