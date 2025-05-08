class Logger:

    def __init__(self):
        self.prev = {}
        self.time = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.prev.get(message,-inf) > timestamp - 10:
            return False
        self.prev[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)