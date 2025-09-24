class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)

        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        result.append(".")
        remainder_idx = {}
        decimals = []

        while remainder != 0:
            if remainder in remainder_idx:
                idx = remainder_idx[remainder]
                decimals.insert(idx, "(")
                decimals.append(")")
                break
            remainder_idx[remainder] = len(decimals)
            remainder *= 10
            decimals.append(str(remainder // denominator))
            remainder %= denominator
        result.extend(decimals)
        return "".join(result)

