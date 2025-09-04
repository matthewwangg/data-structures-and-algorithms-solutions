import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital, profit) for profit, capital in zip(profits, capital)]
        projects.sort()

        heap = []
        projects_enqueued, projects_completed = 0, 0
        final_capital = w

        if w < projects[0][0]:
            return final_capital

        while projects_completed < k:
            while projects_enqueued < len(projects) and projects[projects_enqueued][0] <= final_capital:
                heapq.heappush(heap, -projects[projects_enqueued][1])
                projects_enqueued += 1

            if not heap:
                break

            profit = -heapq.heappop(heap)

            final_capital += profit
            projects_completed += 1

        return final_capital
