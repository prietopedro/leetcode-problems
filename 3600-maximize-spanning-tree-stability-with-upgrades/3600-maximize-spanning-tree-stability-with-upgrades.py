class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class UnionFind:
            def __init__(self, n):
                self.root = [ i for i in range(n)]
                self.rank = [ 1 ] * n
                self.cc = n
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x]) # path compression optimized
                return self.root[x]
            def union(self, x, y):
                X, Y = self.find(x), self.find(y)
                if X == Y:
                    return False
                elif self.rank[X] > self.rank[Y]:   #union by rank optimized 
                    self.root[Y] = X
                elif self.rank[Y] > self.rank[X]:
                    self.root[X] = Y
                else:
                    self.root[Y] = X
                    self.rank[X] += 1
                self.cc -= 1
                return True
            def are_connected(self, u, v):
                U, V = self.find(u), self.find(v)
                if U == V:
                    return True
                return False

        ans = math.inf
        ds = UnionFind(n)
        must_count = 0
        for u, v , s, must in edges:
            if must:
                ans = min(ans, s)
                if ds.union(u, v):
                    must_count += 1
                else:
                    return -1
        cut_edges = []
        need = n - 1 - must_count
        for u, v, s, must in edges:
            if must or ds.are_connected(u, v):
                continue
            cut_edges.append((-s, u, v)) #max heap based on strengths 
        heapq.heapify(cut_edges)
        while need > 0:
            if not cut_edges:
                return -1
            out = heapq.heappop(cut_edges)
            s, u, v = -out[0], out[1], out[2]
            if not ds.are_connected(u, v):
                if need > k:
                    ans = min(ans, s)
                else:
                    ans = min(ans, 2 * s) #for last k weak edges, we upgrade them to double 
                need -= 1
                ds.union(u, v)
        return ans
            


