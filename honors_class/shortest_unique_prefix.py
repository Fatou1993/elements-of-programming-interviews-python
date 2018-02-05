def shortest_unique_prefix(dict, s):
    trie = Trie()
    for word in dict :
        trie.insert(word)
    trie.insert(s)
    n = len(s)
    for i in range(n):
        substring = s[:(i+1)]
        if trie.is_prefix_one_word(substring):
            return substring
    return ""



class Trie :
    def __init__(self):
        self.alphabet = [None]*26
        self.is_word = False
        self.count_suffixes = 0

    def insert(self, word):
        curr = self
        for c in word :
            idx = ord(c) - ord('a')
            if not curr.alphabet[idx]:
                curr.alphabet[idx] = Trie()
            curr.alphabet[idx].count_suffixes += 1
            curr = curr.alphabet[idx]
        curr.is_word = True


    def is_prefix_one_word(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.alphabet[idx]:
                return True
            curr = curr.alphabet[idx]
        return curr.count_suffixes == 1


if __name__ == "__main__":
    dict = ["dog", "be", "cut", "car"]
    word = "cat"
    print shortest_unique_prefix(dict, word)

