class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        candies_dict = Counter(candies)
        distinct_candies = len(candies_dict.keys())
        if k == 0:
            return distinct_candies
        left = 0
        best = 0
        for right in range(len(candies)):
            right_candy = candies[right]
            candies_dict[right_candy] -= 1
            if candies_dict[right_candy] == 0:
                distinct_candies -= 1
            if right - left + 1 == k:
                left_candy = candies[left]
                best = max(best, distinct_candies)
                candies_dict[left_candy] += 1
                if candies_dict[left_candy] == 1:
                    distinct_candies += 1
                left += 1
        return best
            