class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.connectedComponents = size

    def find(self, element):
        if element != self.parent[element]:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
    def union(self,x,y):
        rootX,rootY = self.find(x),self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        self.connectedComponents -= 1

    def numberOfConnectedComponents(self):
        return self.connectedComponents


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for x,y in edges:
            uf.union(x,y)
        return uf.numberOfConnectedComponents()