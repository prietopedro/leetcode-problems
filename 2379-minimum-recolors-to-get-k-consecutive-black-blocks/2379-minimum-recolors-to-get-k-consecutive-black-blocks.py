class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_counter = 0
        left = 0
        min_changes = inf
        for right in range(len(blocks)):
            black_counter += blocks[right] == 'B'
            if right - left + 1 >= k:
                min_changes = min(min_changes, k - black_counter)
                black_counter -= blocks[left] == 'B'
                left += 1
        return min_changes