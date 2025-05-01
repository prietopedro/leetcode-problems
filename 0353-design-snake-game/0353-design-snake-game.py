class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.row = 0
        self.col = 0
        self.visited = set([(0,0)])
        self.stack = deque([(0,0)])
        self.len = 1
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.status = 1

    def move(self, direction: str) -> int:
        if not self.status:
            return -1
        if direction == "R":
            self.col += 1
        elif direction == "U":
            self.row -= 1
        elif direction == "D":
            self.row += 1
        elif direction == "L":
            self.col -= 1
        coords = (self.row,self.col)
        removed = self.stack.popleft()
        self.visited.remove(removed)
        if coords in self.visited:
            self.status = 0
            return -1
        if 0 > self.row or self.height <= self.row:
            self.status = 0
            return -1
        if 0 > self.col or self.width <= self.col:
            self.status = 0
            return -1

        self.visited.add(coords)
        self.stack.append(coords)
        if self.food_index >= len(self.food):
            return self.len - 1

        if coords == tuple(self.food[self.food_index]):
            self.food_index += 1
            self.len += 1
            self.visited.add(removed)
            self.stack.appendleft(removed)
            
        return self.len - 1
        
            
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)