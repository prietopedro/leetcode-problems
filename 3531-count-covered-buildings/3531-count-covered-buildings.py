class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = {}
        cols = {}
        for x,y in buildings:
            if x not in rows:
                rows[x] = [y,y]
            if y not in cols:
                cols[y] = [x,x]

            rows[x][0],rows[x][1] = min(rows[x][0],y),max(rows[x][1],y)
            cols[y][0],cols[y][1] = min(cols[y][0],x),max(cols[y][1],x)
                
        return sum(cols[y][0] < x < cols[y][-1] and rows[x][0] < y < rows[x][-1] for x,y in buildings)
        
