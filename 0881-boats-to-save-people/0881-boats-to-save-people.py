class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left_index,right_index = 0,len(people) - 1
        output = 0
        people.sort()
        while left_index <= right_index:
            while left_index < right_index and people[left_index] + people[right_index] > limit:
                output += 1
                right_index -= 1
            if left_index < right_index: output += 1
            else: output += 1
            left_index += 1
            right_index -= 1
        return output
            
            