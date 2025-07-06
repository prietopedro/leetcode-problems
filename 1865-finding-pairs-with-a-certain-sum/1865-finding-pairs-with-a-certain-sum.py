class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.nums1_count = Counter(nums1)
        self.nums2_count = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1
        if self.nums2_count[self.nums2[index]] == 0:
            del self.nums2_count[self.nums2[index]]
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        output = 0
        for key,val in self.nums1_count.items():
            if (target := tot - key) in self.nums2_count:
                output += val * self.nums2_count[target]
        return output
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
