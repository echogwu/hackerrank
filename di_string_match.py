"""
https://leetcode.com/contest/weekly-contest-111/problems/di-string-match/
"""


class Solution:

    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        print(n)
        if n == 0:
            return []
        letter = S[0]
        small = 0
        large = n
        result = []
        if S[0] == "I":
            result.append(0)
            small = 1
        else:
            result.append(n)
            large = n - 1
        print(result)
        counter = 1
        i = 1
        while i < n:
            print(i)
            if S[i] == letter:
                i += 1
                counter += 1
                continue
            else:
                if letter == "I":
                    result += list(range(large - counter + 1, large + 1))
                    large -= counter
                    print(result)
                else:
                    result += list(range(small + counter - 1, small - 1, -1))
                    small += counter
                    print(result)

                letter = S[i]
                i += 1
                counter = 1
        if S[n - 1] == "I":
            result += list(range(small, large + 1))
        else:
            result += list(range(large, small - 1, -1))
        return result


S = "III"
s = Solution()
print(s.diStringMatch(S))
