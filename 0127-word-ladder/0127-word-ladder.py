class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        graph = defaultdict(list)
        newWordList = wordList + [beginWord]
        for i in range(len(newWordList)):
            for j in range(i + 1, len(newWordList)):
                word1,word2 = newWordList[i],newWordList[j]
                w1,w2 = 0,0
                changes = 0
                while w1 < len(word1) and w2 < len(word2):
                    if word1[w1] != word2[w2]:
                        if changes:
                            break
                        changes += 1
                    w1 += 1
                    w2 += 1
                if w1 == len(word1) and w2 == len(word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        visited = set()
        visited.add(beginWord)
        q = deque([(beginWord,1)])
        while q:
            curr,level = q.popleft()
            if curr == endWord:
                return level
            
            for nei in graph[curr]:
                if nei in visited:
                    continue
                visited.add(nei)
                q.append((nei,level + 1))
        return 0


        