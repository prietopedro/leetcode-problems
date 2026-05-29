class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = {'2','3','4','5','7'}
        rotate = {'6': '9', '9': '6'}

        strNum = str(n)
        output = []
        for i in range(len(strNum) - 1, -1, -1):
            if strNum[i] in invalid:
                return False
            elif strNum[i] in rotate:
                output.append(rotate[strNum[i]])
            else:
                output.append(strNum[i])
        return int("".join(output)) != n