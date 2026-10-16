class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        classes = defaultdict(list)
        has_prereq = set()
        for course,prerequisite in prerequisites:
            indegree[course] += 1
            classes[prerequisite].append(course)
            has_prereq.add(course)
        q = deque([])
        courses_taken = []
        for i in range(numCourses):
            if i not in has_prereq:
                q.append(i)

        while q:
            course = q.popleft()
            courses_taken.append(course)
            for next_course in classes[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        if len(courses_taken) != numCourses:
            return []
        return courses_taken

        
