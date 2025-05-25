class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def isPrime(num):
            if num == 1: return False
            for i in range(2,int(sqrt(num) + 1)):
                if num % i == 0:
                    return False
            return True
            
        best = []
        seen = set()
        for i in range(len(s)):
            current = 0
            if s[i] == '0': continue
            for j in range(i,len(s)):
                current = (current * 10) + int(s[j])
                if isPrime(current) and current not in seen:
                    heapq.heappush(best,current)
                    seen.add(current)
                if len(best) > 3:
                    heapq.heappop(best)
                
        return sum(best)
                
                
            