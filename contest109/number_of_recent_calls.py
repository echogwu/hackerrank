class RecentCounter:

    def __init__(self):
        self.record = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.record.append(t)
        n = len(self.record)
        for i in range(n):
            if t - self.record[i] <= 3000:
                break
        self.record = self.record[i:]
        # print(self.record)

        return len(self.record)


c = RecentCounter()
print(c.ping(1))
print(c.ping(100))
print(c.ping(3001))
print(c.ping(3002))
