class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #take current + partition rest
        #if len() == 1, check next if its same, + partition rest
        #check before and after

        # 'aaa'
        # 'a' + partition('aa')
        # 'a' + 'a' + partition('a') 
        # 'a' + 'a' + 'a'

        curr = []
        output = []
        def backtrack(j):
            if j >= len(s):
                if sum(len(x) for x in curr) == len(s):
                    output.append(curr[:])
                return
            
            for i in range(j, len(s)):
                left = i
                right = i
                while left >= j and right < len(s) and s[left] == s[right]:
                    curr.append(s[left:right + 1])
                    backtrack(right + 1)
                    curr.pop()
                    left -= 1
                    right += 1
                left = i
                right = i + 1
                while left >= j and right < len(s) and s[left] == s[right]:
                    curr.append(s[left:right + 1])
                    backtrack(right + 1)
                    curr.pop()
                    left -= 1
                    right += 1
        backtrack(0)
        return output