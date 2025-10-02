class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        full = numBottles
        empty = 0
        exch= numExchange
        while full > 0:
            total += full
            empty += full
            full = 0
            if empty >= exch:
                empty -= exch
                full = 1
                exch += 1
            else:
                break
        return total