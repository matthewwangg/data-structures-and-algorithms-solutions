import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        meetings_per_room = defaultdict(int)

        events = []
        free_rooms = []

        for room in range(n):
            heapq.heappush(free_rooms, room)

        for meeting in meetings:
            while events:
                end_time, room = heapq.heappop(events)
                if meeting[0] >= end_time:
                    heapq.heappush(free_rooms, room)
                else:
                    heapq.heappush(events, (end_time, room))
                    break

            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(events, (meeting[1], room))
            else:
                end_time, room = heapq.heappop(events)
                heapq.heappush(events, (end_time+(meeting[1]-meeting[0]), room))
            
            meetings_per_room[room] += 1

        room, meeting_count = float('inf'), 0
        for key in meetings_per_room:
            if meetings_per_room[key] > meeting_count or (meetings_per_room[key] == meeting_count and key < room):
                room, meeting_count = key, meetings_per_room[key]
            
        return room
