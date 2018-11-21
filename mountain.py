class Solution:

    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        n = len(A)
        print(n)
        i = 0
        while i < n - 1:
            if A[i] < A[i + 1]:
                print(A[i], A[i + 1])
                i += 1
            else:
                break

        if i == n - 1 or i == 0:
            return False
        for j in range(i + 1, n):
            if A[i] > A[j]:
                i = j
                continue
            else:
                return False
        return True


arr = [3, 5, 5, 2]
s = Solution()
print(s.validMountainArray(arr))
