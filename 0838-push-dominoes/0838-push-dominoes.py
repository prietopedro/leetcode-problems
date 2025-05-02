class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque([])
        seen = set()
        output = [c for c in dominoes]
        for i,domino in enumerate(dominoes):
            if domino in "RL":
                seen.add(i)
                q.append(i)
        while q:
            next_level = defaultdict(int)
            for _ in range(len(q)):
                curr = q.popleft()
                if output[curr] == 'L': next_level[curr - 1] -= 1
                if output[curr] == 'R': next_level[curr + 1] += 1
            for key,val in next_level.items():
                if val != 0 and 0 <= key < len(dominoes) and key not in seen:
                    seen.add(key)
                    q.append(key)
                    output[key] = 'R' if val == 1 else 'L'
        return ''.join(output)
                