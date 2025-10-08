class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            # minimum potion strength required
            minPotion = math.ceil(success / spell)
            # find index where potions >= minPotion
            idx = bisect_left(potions, minPotion)
            # count of successful potions
            res.append(m - idx)

        return res