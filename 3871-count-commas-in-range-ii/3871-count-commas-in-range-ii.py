class Solution:
    def countCommas(self, n: int) -> int:
        # 1000-9999 -> 1
        # 10,000-99,999 -> 1
        # 100,000-999,999 -> 1
        # 1,000,000-999,999,999 -> 2

        current = 1000
        loop = 1
        total = 0
        while n >= current:
            nxt = current * 1000
            max_num = min(n,nxt - 1)
            total += (max_num - current + 1) * loop
            current = nxt
            loop += 1
        return total
