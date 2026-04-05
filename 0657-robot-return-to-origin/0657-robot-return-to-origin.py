class Solution:
    def judgeCircle(self, moves: str) -> bool:
        store = defaultdict(int)
        for move in moves:
            store[move] += 1
        return store["U"] == store["D"] and store["L"] == store["R"]