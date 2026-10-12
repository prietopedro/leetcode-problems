class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        s = [(self.root, 0)]

        while s:
            curr, i = s.pop()

            if i == len(word):
                if curr.isWord:
                    return True
                continue

            if word[i] == ".":
                for child in curr.children.values():
                    s.append((child, i + 1))
            elif word[i] in curr.children:
                s.append((curr.children[word[i]], i + 1))

        return False

            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)