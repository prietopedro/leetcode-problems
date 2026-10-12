
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Trie:
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
        if not board or not board[0]:
            return []

        trie_g = Trie()
        for word in words:
            trie_g.add(word)

        seen = set()
        output = []
        m, n = len(board), len(board[0])

        def recurse(row, col, parent, char):
            if not (0 <= row < m and 0 <= col < n):
                return
            if (row, col) in seen:
                return
            if char not in parent.children:
                return

            trie = parent.children[char]

            if trie.word:
                output.append(trie.word)
                trie.word = ""

            seen.add((row, col))

            for nr, nc in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]:
                if 0 <= nr < m and 0 <= nc < n:
                    next_char = board[nr][nc]
                    recurse(nr, nc, trie, next_char)

            seen.remove((row, col))

            # Remove this Trie branch if nothing remains
            if not trie.children and not trie.word:
                del parent.children[char]

        for row in range(m):
            for col in range(n):
                char = board[row][col]
                recurse(row, col, trie_g.root, char)

        return output
