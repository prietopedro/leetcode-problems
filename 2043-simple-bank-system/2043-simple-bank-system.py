class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid(account1) or not self.valid(account2):
            return False
        if not self.withdraw(account1,money):
            return False
        return self.deposit(account2,money)

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account): return False
        index = account - 1
        self.balance[index] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account): return False
        index = account - 1
        if self.balance[index] < money: return False
        self.balance[index] -= money
        return True

    
    def valid(self,account):
        return 1 <= account <= len(self.balance)
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)