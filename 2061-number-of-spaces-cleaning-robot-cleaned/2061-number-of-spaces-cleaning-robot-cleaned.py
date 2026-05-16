class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        seen = set()
        curr = (0,0,90)
        directions = {
            0: (-1,0),
            90: (0,1),
            180: (1,0),
            270: (0,-1)
        }
        cleaned = set()
        while curr not in seen:
            cleaned.add((curr[0],curr[1]))
            seen.add(curr)
            change = directions[curr[2]]
            next_row = curr[0] + change[0]
            next_col = curr[1] + change[1]
            if next_row < 0 or next_row >= len(room) or next_col < 0 or next_col >= len(room[0]) or room[next_row][next_col] == 1:
                curr = (curr[0],curr[1],(curr[2] + 90) % 360)
            else:
                curr = (next_row,next_col,curr[2])
        return len(cleaned)
