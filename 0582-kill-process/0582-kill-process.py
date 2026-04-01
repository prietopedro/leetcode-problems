class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parents = defaultdict(list)
        for i in range(len(ppid)):
            parents[ppid[i]].append(pid[i])

        stack = [kill]
        output = []
        while stack:
            current = stack.pop()
            stack.extend(parents[current])
            output.append(current)
        return output

        