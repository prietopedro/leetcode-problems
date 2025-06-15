class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = (10 ** 9) + 7
        i_seen = defaultdict(int)
        j_seen = defaultdict(int)
        output = 0
        for num in nums:
            if num % 2 == 0:
                output += j_seen[num // 2]
            j_seen[num] += i_seen[num * 2]
            i_seen[num] += 1

            
        return output % mod