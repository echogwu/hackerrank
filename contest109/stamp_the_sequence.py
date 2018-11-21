from collections import Counter


class Solution:

    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        stamp_set = set(list(dict(Counter(stamp)).keys()))
        target_set = set(list(dict(Counter(target)).keys()))
        if stamp_set < target_set:
            return []
