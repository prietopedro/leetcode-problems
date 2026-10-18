class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size  # Rank helps in balancing the tree
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    
    def same_set(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        emails = {}
        for i,acc in enumerate(accounts):
            for j in range(1, len(acc)):
                if acc[j] in emails:
                    uf.union(i,emails[acc[j]])
                emails[acc[j]] = i
        
        output = []
        completed = set()
        for i in range(len(accounts)):
            if i in completed:
                continue
            output.append([])
            for j in range(len(accounts)):
                if j in completed:
                    continue
                if uf.same_set(i,j):
                    output[-1].extend(accounts[j][1:])
                    completed.add(j)
            output[-1] = [accounts[i][0]] + sorted(set(output[-1]))
            completed.add(i)
        return output