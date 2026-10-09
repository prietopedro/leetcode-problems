class Solution:
    def partition(self, s: str) -> list[list[str]]:
        @cache
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True
        output = []
        def bt(start, current):
            print(start, current)
            if len("".join(current)) == len(s):
                output.append(current[:])
                return
            if start >= len(s):
                return

            for j in range(start,len(s)):
                if isPalindrome(s[start:j+1]):
                    current.append(s[start:j+1])
                    bt(j + 1, current)
                    current.pop()

        bt(0,[])
        return output