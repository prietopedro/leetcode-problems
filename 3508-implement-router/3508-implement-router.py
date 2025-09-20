class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.q = deque([])
        self.seen = set()
        self.counts = defaultdict(deque) 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.seen:
            return False
        self.seen.add((source,destination,timestamp))
        self.q.append((source,destination,timestamp))
        self.counts[destination].append(timestamp)
        if len(self.q) > self.memory_limit:
            oldSource,oldDest,timestamp = self.q.popleft()
            self.counts[oldDest].popleft()
            self.seen.remove((oldSource,oldDest,timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        oldSource,oldDest,timestamp = self.q.popleft()
        self.counts[oldDest].popleft()
        self.seen.remove((oldSource,oldDest,timestamp))
        return [oldSource,oldDest,timestamp]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0

        # Binary search for range
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)