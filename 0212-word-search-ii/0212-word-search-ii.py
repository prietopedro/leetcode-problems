class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = ""
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie_g = Trie()
        for word in words:
            trie_g.add(word)

        seen = set()
        output = []
        m,n = len(board),len(board[0])
        num = 1
        def recurse(row,col,trie):
            if not (0 <= row < m and 0 <= col < n):
                return
            if (row,col) in seen:
                return
            if board[row][col] not in trie.children:
                return
            trie = trie.children[board[row][col]]
            if trie.word:
                output.append(trie.word)     
            seen.add((row,col))
            recurse(row + 1, col, trie)
            recurse(row - 1, col, trie)
            recurse(row, col + 1, trie)
            recurse(row, col - 1, trie)
            seen.remove((row,col))


        for row in range(m):
            for col in range(n):
                recurse(row,col,trie_g.root)
        return list(set(output))