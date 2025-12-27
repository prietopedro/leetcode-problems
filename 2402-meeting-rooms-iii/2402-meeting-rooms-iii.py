class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = []
        taken_rooms = []
        for i in range(n):
            available_rooms.append((i))
        meetings.sort(key=lambda x: x[0])

        time = 0
        meetings_counter = defaultdict(int)
        best_room,best_room_count = 0,0
        times = defaultdict(int)
        for i, (start,end) in enumerate(meetings):
            time = start
            while (taken_rooms and taken_rooms[0][0] <= start) or not available_rooms:
                available_time,room = heapq.heappop(taken_rooms)
                times[room] = available_time
                heapq.heappush(available_rooms,room)

            room = heapq.heappop(available_rooms)
            available_time = times[room]
            time = max(available_time,start)

            meetings_counter[room] += 1

            if meetings_counter[room] > best_room_count:
                best_room,best_room_count = room,meetings_counter[room]
            elif meetings_counter[room] == best_room_count:
                best_room = min(best_room,room)

            heapq.heappush(taken_rooms,(time + end - start, room))

        return best_room

        # 0,1,2,3
        # [[2,13],[3,12],[7,10],[17,19],[18,19]]

        # [2,13]
        # {0 -> 1}
        # 0 -> 13
        # time = 2

        # [3,12]
        # {0 -> 1, 1 -> 1}
        # time = 3



            


