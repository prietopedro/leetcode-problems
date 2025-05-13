class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count=[0 for i in range(26)]
        a = ord("a")
        for i in s:
            count[ord(i)-a]+=1
        for i in range(t):
            count.insert(0, count.pop(-1))
            count[1]+= count[0]
        return sum(count)%(10**9 +7)   