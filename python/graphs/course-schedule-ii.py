class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {}
        q = deque()
        for i in range(numCourses):
            prereqs[i] = set()

        for i in prerequisites:
            if i[0] == i[1]:
                return False
            prereqs[i[0]].add(i[1])

        for c in prereqs:
            if len(prereqs[c]) == 0:
                q.append(c)

        done = []
        while q:
            current = q.popleft()
            done.append(current)

            if len(done) == numCourses:
                return done

            for c in prereqs:
                if current in prereqs[c]:
                    prereqs[c].remove(current)
                    if not prereqs[c]:
                        q.append(c)

        return []