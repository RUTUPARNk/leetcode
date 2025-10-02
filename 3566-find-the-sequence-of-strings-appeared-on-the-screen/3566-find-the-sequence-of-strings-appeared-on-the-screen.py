class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        curr = []
        for c in target:
            presses = ord(c) - ord('a')
            curr.append("a")
            ans.append("".join(curr))
            for i in range(1, presses + 1):
                curr.pop()
                curr.append(chr(i + ord('a')))
                ans.append("".join(curr))
        return ans

