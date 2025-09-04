import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        string = ""

        while heap:
            negative_count, letter = heapq.heappop(heap)
            count = abs(negative_count)

            if len(string) > 1 and letter == string[-1] and letter == string[-2]:
                if not heap:
                    return string

                second_negative_count, second_letter = heapq.heappop(heap)
                second_count = abs(second_negative_count)

                string += second_letter
                if second_count - 1 > 0:
                    heapq.heappush(heap, (-(second_count - 1), second_letter))

                heapq.heappush(heap, (-count, letter))
            else:
                string += letter
                if count - 1 > 0:
                    heapq.heappush(heap, (-(count - 1), letter))

        return string
