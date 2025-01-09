import queue


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = queue.PriorityQueue()
        lastseen = {}
        count = {}
        used = {}
        for task in tasks:
            lastseen[task] = -n
            count[task] = count.get(task, 0) + 1

        for task in count.keys():
            q.put((-count[task], task))

        finalcount = 0
        while len(q.queue) > 0:
            current = q.get()
            if current[0]:
                count = lastseen[current[1]] + n + 1
                while count in used:
                    count += 1
                lastseen[current[1]] = count
                used[count] = 1
                finalcount = max(finalcount, count)
                q.put((current[0] + 1, current[1]))

        return finalcount