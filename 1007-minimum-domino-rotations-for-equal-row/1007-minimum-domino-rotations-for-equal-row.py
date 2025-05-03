class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        curr_top,curr_bot = tops[0],bottoms[0]
        curr_top_inverse,curr_bot_inverse = bottoms[0],tops[0]
        top_counter,bot_counter = 0,0
        top_counter_inverse,bot_counter_inverse = 0,0
        for num1,num2 in zip(tops,bottoms):
            if num1 != curr_top:
                if num2 != curr_top:
                    top_counter = inf
                top_counter += 1
            if num2 != curr_bot:
                if num1 != curr_bot:
                    bot_counter = inf
                bot_counter += 1
            if num1 != curr_top_inverse:
                if num2 != curr_top_inverse:
                    top_counter_inverse = inf
                top_counter_inverse += 1
            if num2 != curr_bot_inverse:
                if num1 != curr_bot_inverse:
                    bot_counter_inverse = inf
                bot_counter_inverse += 1
        best = min(top_counter,bot_counter,top_counter_inverse,bot_counter_inverse)
        return best if best != inf else -1
    