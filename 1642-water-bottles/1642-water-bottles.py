class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empties = numBottles
        while empties >= numExchange:
            newBottles = empties // numExchange
            total += newBottles
            empties = (empties % numExchange) + newBottles
        return total