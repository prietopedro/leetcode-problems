class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_arr = [num for num in str(num)]
        max_num_replace = 0
        while max_num_replace < len(str_arr) and str_arr[max_num_replace] == '9':
            max_num_replace += 1

        max_num = int(''.join('9' if max_num_replace < len(str_arr) and num == str_arr[max_num_replace] else num for num in str_arr))
        min_num = int(''.join('0' if num == str_arr[0] else num for num in str_arr))
        print(max_num,min_num)
        return max_num - min_num
        