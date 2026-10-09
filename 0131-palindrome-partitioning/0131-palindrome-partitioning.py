class Solution:
    def partition(self, s: str) -> list[list[str]]:
        @cache
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        output = []
        def bt(start, current):
            if start == len(s):
                output.append(current[:])
                return

            if start >= len(s):
                return

            for j in range(start,len(s)):
                if isPalindrome(start,j):
                    current.append(s[start:j+1])
                    bt(j + 1, current)
                    current.pop()

        bt(0,[])
        return output