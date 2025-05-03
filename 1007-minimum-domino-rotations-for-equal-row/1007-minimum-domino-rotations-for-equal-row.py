class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        curr_top,curr_bot = tops[0],bottoms[0]
        curr_top_inverse,curr_bot_inverse = bottoms[0],tops[0]
        top_counter,bot_counter = 0,0
        top_counter_inverse,bot_counter_inverse = 0,0
        def count(num,inverse,against):
            if num == against:
                return 0
            if inverse != against:
                return inf
            return 1
        for num1,num2 in zip(tops,bottoms):
            top_counter += count(num1,num2,curr_top)
            bot_counter += count(num2,num1,curr_bot)
            top_counter_inverse += count(num1,num2,curr_top_inverse)
            bot_counter_inverse += count(num2,num1,curr_bot_inverse)
        best = min(top_counter,bot_counter,top_counter_inverse,bot_counter_inverse)
        return best if best != inf else -1
    