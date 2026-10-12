class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m,n = len(rooms),len(rooms[0])
        q = deque([])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2147483647
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row,col))

        level = 1
        while q:

            for _ in range(len(q)):
                row,col = q.popleft()
                # if rooms[row][col] == 0:
                #     rooms[row][col] = level

                for dr,dc in dirs:
                    nr,nc = row + dr,col + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if rooms[nr][nc] != INF:
                        continue 
                    q.append((nr,nc))
                    rooms[nr][nc] = level
            level += 1


