class Solution:

    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        x_tmp = defaultdict(set)
        x_map = {}
        for i in points:
            x_tmp[i[0]].add(i[1])

        for x, y in x_tmp.items():
            if len(y) < 2:
                continue
            x_map[x] = y

        print(x_map)
        mini_area = float("inf")
        keys = list(x_map.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                overlap = x_map[keys[i]] & x_map[keys[j]]
                if len(overlap) >= 2:
                    overlap = list(overlap)
                    overlap.sort()
                    dis = min(abs(overlap[n] - overlap[n + 1]) for n in range(len(overlap) - 1))
                    area = abs(keys[i] - keys[j]) * dis
                    if area < mini_area:
                        mini_area = area
        if mini_area == float("inf"):
            return 0
        return mini_area


points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
s = Solution()
print(s.minAreaRect(points))
