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
        
        groups = defaultdict(set)

        for i, acc in enumerate(accounts):
            root = uf.find(i)
            groups[root].update(acc[1:])

        output = []

        for root, email_set in groups.items():
            name = accounts[root][0]
            output.append([name] + sorted(email_set))

        return output