class Solution:

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        small, large = -1, -1
        n = len(nums)
        if n == 0:
            return [-1, -1]
        small, large = self.search(nums, 0, n - 1, target)

        return [small, large]

    def search(self, nums, start, end, target):
        print(start, end)
        if start > end:
            return -1, -1
        middle = (start + end) // 2
        print(f"middle: {middle}")
        if nums[middle] == target:
            small_left, large_left = self.search(nums, start, middle - 1, target)
            small_right, large_right = self.search(nums, middle + 1, end, target)
            small = small_left if small_left != -1 else middle
            large = large_right if large_right != -1 else middle
        elif nums[middle] < target:
            small, large = self.search(nums, middle + 1, end, target)
        else:
            small, large = self.search(nums, start, middle - 1, target)
        return small, large


nums = [5, 7, 7, 8, 8, 10]
target = 10
s = Solution()
print(s.searchRange(nums, target))
