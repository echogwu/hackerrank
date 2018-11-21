class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        valid_len = 0
        if len(nums1) == 0:
            valid_len = len(nums2)
            valid_array = nums2
        if len(nums2) == 0:
            valid_len = len(nums1)
            valid_array = nums1
        if valid_len:
            if valid_len % 2 == 0:
                return (valid_array[valid_len / 2 - 1] + valid_array[valid_len / 2]) / 2
            else:
                return valid_array[valid_len // 2]

        return self.findMedian(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1)

    def findMedian(self, nums1, s1, e1, nums2, s2, e2):
        print(f"s1: {s1}, e1: {e1}, s2: {s2}, e2: {e2}")
        if s1 == e1:
            return max(nums1[s1], nums2[(s2 + e2) // 2])
        if s2 == e2:
            return max(nums2[s2], nums1[(s1 + e1) // 2])

        i = (s1 + e1) // 2
        j = (s2 + e2) // 2
        print(f"i: {i}, j: {j}")
        if nums1[i] == nums1[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            return self.findMedian(nums1, i, e1, nums2, s1, j)
        else:
            return self.findMedian(nums1, s1, i, nums2, j, e2)


nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [2, 7, 8]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
