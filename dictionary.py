class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = []

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = len(word)
        hash_value = 0
        expo = n - 1
        for w in word:
            w = ord(w) - ord("a") + 1
            hash_value += w * pow(27, expo)
            expo -= 1
        self.index.append(hash_value)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        first = self.index
        # print(first)
        for i in range(n - 1, 0, -1):
            w = word[i]
            # print(w)
            if w == ".":
                tmp = [i // 27 for i in first]
                first = [i for i in tmp if i != 0]
                # print(first)
            else:
                tmp = [i // 27 for i in first if i % 27 == (ord(w) - ord("a") + 1)]
                first = [i for i in tmp if i != 0]
                # print(first)

        w = word[0]
        if (w == "." and any([i < 27 for i in first])) or (word[0] != "." and (ord(w) - ord("a") + 1) in first):
            # print(True)
            return True
        else:
            # print(False)
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.index)
print(obj.search("pad"))
print(obj.search("bad"))
