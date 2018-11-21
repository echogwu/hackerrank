class Solution:

    def numSubarraysWithSum_1(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if A == [] or sum(A) < S or (sum(A) == len(A) and S == 0):
            return 0
        ones = [i for i in range(len(A)) if A[i] == 1]
        counter = []
        for i in range(len(ones)):
            if i == 0:
                counter.append(ones[i])
            else:
                counter.append(ones[i] - ones[i - 1] - 1)
        if len(ones) == 0:
            counter.append(len(A))
        else:
            counter.append(len(A) - ones[-1] - 1)
        if S == 0:
            return int(sum(i * (i + 1) / 2 for i in counter))
        else:
            s = 0
            for i in range(len(ones) - S + 1):
                s += (counter[i] + 1) * (counter[i + S] + 1)
            return int(s)

    def numSubarraysWithSum(self, A, S):
        import collections
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
            print(dict(c), psum, res)
        return res


s = Solution()
A = [1, 0, 1, 0, 1]
S = 2
print(A)
print(s.numSubarraysWithSum(A, S))
