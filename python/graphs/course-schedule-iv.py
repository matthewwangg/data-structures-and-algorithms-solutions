class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = {}
        reverse_prereqs, indegrees = {}, {}

        for prereq in prerequisites:
            if prereq[1] not in prereqs:
                prereqs[prereq[1]] = set()
            prereqs[prereq[1]].add(prereq[0])

            if prereq[0] not in reverse_prereqs:
                reverse_prereqs[prereq[0]] = []
            reverse_prereqs[prereq[0]].append(prereq[1])
            indegrees[prereq[1]] = indegrees.get(prereq[1], 0) + 1
        
        topological_order = []
        q = deque()

        for course in range(numCourses):
            if not prereqs.get(course, set()):
                q.append(course)
        
        while q:
            current = q.popleft()
            topological_order.append(current)

            for next_course in reverse_prereqs.get(current, []):
                indegrees[next_course] = indegrees.get(next_course, 0) - 1
                if indegrees[next_course] == 0:
                    q.append(next_course)
        
        for course in topological_order:
            for prereq in prereqs.get(course, set()):
                prereqs[course] = prereqs.get(course, set()).union(prereqs.get(prereq, set()))
        
        answer = []
        for query in queries:
            if query[0] in prereqs.get(query[1], set()):
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
