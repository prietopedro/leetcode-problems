class UF:
    def __init__(self,n):
        self.p = [i for i in range(n)]
        self.w = [1 for _ in range(n)]
    def find(self,i):
        curr = i
        while curr != self.p[curr]:
            self.p[curr] = self.p[self.p[curr]]
            curr = self.p[curr]
        return curr
    def union(self,i,j):
        p1,p2 = self.find(i),self.find(j)
        if p1 == p2:
            return True
        if self.w[p1] > self.w[p2]:
            self.w[p1] += self.w[p2]
            self.p[p2] = p1
        else:
            self.w[p2] += self.w[p1]
            self.p[p1] = p2
        
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UF(n)
        left = 0
        for right in range(1,n):
            while abs(nums[right] - nums[left]) > maxDiff:
                left += 1
            uf.union(left,right)
                
        output = []
        for i,j in queries:
            output.append(uf.find(i) == uf.find(j))
        return output
        