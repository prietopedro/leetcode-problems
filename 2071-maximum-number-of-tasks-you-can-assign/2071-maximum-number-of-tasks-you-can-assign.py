class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # WHY DONT THIS WORK???!!!
        # tasks.sort()
        # workers.sort()

        # def can_complete(m):
        #     task_index = 0
        #     pills_remaining = pills 
        #     new_workers = [(s,0) for s in workers[len(workers) - m:]]
        #     for i in range(m):
        #         while new_workers[0][0] < tasks[i]:
        #             worker_strength,used = heapq.heappop(new_workers)
        #             if not pills_remaining or used: return False
        #             heapq.heappush(new_workers,(worker_strength + strength,1))
        #             pills_remaining -= 1
        #         heapq.heappop(new_workers)

        #     return True

        # low = 1
        # high = min(len(tasks),len(workers)) + 1
        # while low < high:
        #     middle = (low + high) // 2
        #     print(middle,can_complete(middle))
        #     if not can_complete(middle):
        #         high = middle
        #     else:
        #         low = middle + 1
        # return low - 1
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            ws = deque()
            ptr = m - 1
            # Enumerate each task from largest to smallest
            for i in range(mid - 1, -1, -1):
                while ptr >= m - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr -= 1
                if not ws:
                    return False
                # If the largest element in the deque is greater than or equal to tasks[i]
                elif ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    ws.popleft()
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans