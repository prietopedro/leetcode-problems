class Solution:
    def minOperations(self, s: str) -> int:
        # pick middle at each iteration
        # pick curent + 1 as middle (2 middles)

        def getIncrement(letterA,letterB):
            return min(abs(ord(letterA) - ord(letterB)), 26 - (abs(ord(letterA) - ord(letterB))))
   

        def getChanges(left,right, newString):
            changes = 0
            print(left,right)
            while left >= 0 and right < len(s):
                if newString[left] != newString[right]:
                    changes += getIncrement(newString[left], newString[right])
                left -= 1
                right += 1

            return changes

        def shiftString(string):
            output = []
            for i in range(1,len(string)):
                output.append(string[i])
            output.append(string[0])
            return "".join(output)

        curr = s
        shifts = 0
        middle = len(s) // 2
        best = inf
        for _ in range(len(s)):
            if len(s) % 2 == 0:
                count = getChanges(middle - 1,middle,curr)
                best = min(best, count + shifts)
            else:
                count = getChanges(middle,middle,curr)
                best = min(best, count + shifts)
            curr = shiftString(curr)
            shifts += 1
        return best


            