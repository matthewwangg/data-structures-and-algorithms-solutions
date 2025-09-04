import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        string = ""
        heap = []
        for char in count:
            heapq.heappush(heap, (-count[char], char))

        while heap:
            negative_counter, character = heapq.heappop(heap)
            counter = -negative_counter

            if string and character == string[-1]:
                if not heap:
                    return ""

                new_negative_counter, new_character = heapq.heappop(heap)
                new_counter = -new_negative_counter

                string += new_character

                heapq.heappush(heap, (-counter, character))

                if new_counter > 1:
                    heapq.heappush(heap, (-(new_counter - 1), new_character))
            else:
                string += character

                if counter > 1:
                    heapq.heappush(heap, (-(counter - 1), character))

        return string
