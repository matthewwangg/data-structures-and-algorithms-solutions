import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        order = {}

        sorted_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        sorted_tasks.sort()

        heapq.heappush(heap, (sorted_tasks[0][1], sorted_tasks[0][2], sorted_tasks[0][0]))
        tasks_completed, tasks_enqueued = 0, 1
        time = 0

        while heap:
            processing_time, index, enqueued_time = heapq.heappop(heap)
            time = max(time, enqueued_time)

            time += processing_time

            order[index] = tasks_completed
            tasks_completed += 1

            while tasks_enqueued < len(tasks) and sorted_tasks[tasks_enqueued][0] <= time:
                heapq.heappush(heap, (
                sorted_tasks[tasks_enqueued][1], sorted_tasks[tasks_enqueued][2], sorted_tasks[tasks_enqueued][0]))
                tasks_enqueued += 1

            if not heap and tasks_enqueued < len(tasks):
                heapq.heappush(heap, (
                sorted_tasks[tasks_enqueued][1], sorted_tasks[tasks_enqueued][2], sorted_tasks[tasks_enqueued][0]))
                tasks_enqueued += 1

        final_order = [0 for _ in range(len(tasks))]

        for key in order:
            final_order[order[key]] = key

        return final_order
