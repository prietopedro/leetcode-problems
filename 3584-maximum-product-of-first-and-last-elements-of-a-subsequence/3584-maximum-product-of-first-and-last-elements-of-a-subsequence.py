class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        min_num = inf
        max_num = -inf
        buffer = deque([])
        output = -inf
        for num in nums:
            buffer.append(num)
            if len(buffer) == m:
                curr = buffer.popleft()
                min_num = min(curr,min_num)
                max_num = max(curr,max_num)
                output = max(output,min_num * num,max_num * num)
        return output
                
        