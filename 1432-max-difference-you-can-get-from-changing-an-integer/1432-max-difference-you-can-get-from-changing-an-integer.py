class Solution:
    def maxDiff(self, num: int) -> int:
        num_arr = str(num)
        max_num = num
        min_num = num
        max_num_to_replace = num_arr[0]
        min_num_to_replace = num_arr[0]
        if num_arr[0] == '9':
            for c in num_arr:
                if c != '9':
                    max_num_to_replace = c
                    break
        if num_arr[0] == '1':
            for c in num_arr:
                if c != min_num_to_replace and c != '0':
                    min_num_to_replace = c
                    break
        max_num =     int(num_arr.replace(max_num_to_replace,'9'))
        min_num = int(num_arr.replace(min_num_to_replace,'0' if num_arr[0] != min_num_to_replace else '1'))
        return max_num - min_num
        

923456
103456
