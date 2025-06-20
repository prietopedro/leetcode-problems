class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        seen_positives_x = 0
        seen_negatives_x = 0
        seen_positives_y = 0
        seen_negatives_y = 0
        best = 0
        for c in s:
            if c == "N": 
                seen_positives_y += 1
            if c == "S": 
                seen_negatives_y += 1
            if c == "W": 
                seen_positives_x += 1
            if c == "E": 
                seen_negatives_x += 1
            changes = k
            x = seen_positives_x - seen_negatives_x
            y = seen_positives_y - seen_negatives_y
            curr_distance = abs(seen_positives_x - seen_negatives_x) + abs(seen_positives_y - seen_negatives_y)
            if y >= 0 and seen_negatives_y:
                change = min(changes,seen_negatives_y)
                changes -= change
                curr_distance += (change * 2)
            elif y < 0 and seen_positives_y:
                change = min(changes,seen_positives_y)
                changes -= change
                curr_distance += (change  * 2) 
            if x >= 0 and seen_negatives_x:
                change = min(changes,seen_negatives_x)
                changes -= change
                curr_distance += (change * 2)
            elif x < 0 and seen_positives_x:
                change = min(changes,seen_positives_x)
                changes -= change
                curr_distance += (change * 2)

            best = max(best,curr_distance)
        return best

        

                