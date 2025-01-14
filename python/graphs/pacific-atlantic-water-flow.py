class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        visited = set()

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque()

        # Pacific
        for i in range(len(heights)):
            q.append((i, 0, heights[i][0]))
        for i in range(len(heights[0])):
            q.append((0, i, heights[0][i]))

        while q:
            pos = q.popleft()

            if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(heights) or pos[1] >= len(heights[0]) or pos[2] > \
                    heights[pos[0]][pos[1]] or (pos[0], pos[1]) in visited:
                continue

            pacific.add((pos[0], pos[1]))
            visited.add((pos[0], pos[1]))

            for n in neighbors:
                q.append((pos[0] + n[0], pos[1] + n[1], heights[pos[0]][pos[1]]))

        visited = set()

        # Atlantic
        for i in range(len(heights)):
            q.append((i, len(heights[0]) - 1, heights[i][len(heights[0]) - 1]))
        for i in range(len(heights[0])):
            q.append((len(heights) - 1, i, heights[len(heights) - 1][i]))

        while q:
            pos = q.popleft()

            if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(heights) or pos[1] >= len(heights[0]) or pos[2] > \
                    heights[pos[0]][pos[1]] or (pos[0], pos[1]) in visited:
                continue

            atlantic.add((pos[0], pos[1]))
            visited.add((pos[0], pos[1]))

            for n in neighbors:
                q.append((pos[0] + n[0], pos[1] + n[1], heights[pos[0]][pos[1]]))

        return list(atlantic.intersection(pacific))

