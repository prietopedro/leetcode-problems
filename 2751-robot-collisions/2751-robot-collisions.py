class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = {}
        sorted_robots = []
        for i,position in enumerate(positions):
            robots[i] = healths[i]
            sorted_robots.append((position,i))
        
        sorted_robots.sort()

        stack = []
        for position,i in sorted_robots:
            if directions[i] == "R":
                stack.append(i)
                continue

            while stack and robots[i] > 0:
                if robots[stack[-1]] > robots[i]:
                    robots[stack[-1]] -= 1
                    robots[i] = 0
                elif robots[stack[-1]] == robots[i]:
                    robots[stack[-1]] = 0
                    robots[i] = 0
                    stack.pop()
                else:
                    robots[stack[-1]] = 0
                    stack.pop()
                    robots[i] -= 1
        output = []
        for i in range(len(positions)):
            if robots[i] > 0:
                output.append(robots[i])
        return output
            


        