class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance_1,distance_2 = abs(z - x),abs(z - y)
        if distance_1 > distance_2:
            return 2
        elif distance_2 > distance_1:
            return 1
        else:
            return 0