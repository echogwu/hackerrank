"""
943. Find the Shortest Superstring My SubmissionsBack to Contest
User Accepted: 136
User Tried: 415
Total Accepted: 140
Total Submissions: 852
Difficulty: Hard
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Note:

1 <= A.length <= 12
1 <= A[i].length <= 20
"""


class Solution(object):

    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break
        print("overlaps:")
        for i in overlaps:
            print(i)

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1 << N)]
        parent = [[None] * N for _ in xrange(1 << N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        print("dp:")
        for i in xrange(len(dp)):
            print("{}: {}".format(bin(i), dp[i]))
        print("parent:")
        for i in xrange(len(parent)):
            print("{}: {}".format(bin(i), parent[i]))

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1 << N) - 1
        i = max(xrange(N), key=dp[-1].__getitem__)
        print(i)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)


A = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
print(A)
s = Solution()
print(s.shortestSuperstring(A))
