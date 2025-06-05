class DSU:
    def __init__(self):
        self.p = [i for i in range(26)]
        self.w = [0] * 26
        self.min = [i for i in range(26)]
    def find(self,i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return i
    def join(self,i,j):
        p1,p2 = self.find(i),self.find(j)
        if p1 == p2:
            return
        if self.w[p1] < self.w[p2]:
            self.w[p2] += self.w[p1]
            self.p[p1] = p2
            self.min[p2] = min(self.min[p2],self.min[p1])
        else:
            self.w[p1] += self.w[p2]
            self.p[p2] = p1
            self.min[p1] = min(self.min[p1],self.min[p2])
    def get_min(self,i):
        p = self.find(i)
        return self.min[p]     


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()
        c_index = lambda c: ord(c) - ord('a')
        c_char = lambda i: chr(i + ord('a')) 
        for c1,c2 in zip(s1,s2):
            dsu.join(c_index(c1),c_index(c2))
        return ''.join(c_char(dsu.get_min(c_index(c))) for c in baseStr)
