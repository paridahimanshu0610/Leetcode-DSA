import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda x: (x[0], x[1]))

        reservation = []    # Current Reservation
        currRooms = []      # Current Available Rooms

        counter = defaultdict(int) # Keeps track of the room usage frequency

        i = 0
        while i < len(meetings):
            # Reservations that are now available for booking
            while len(reservation) > 0 and reservation[0][0] <= meetings[i][0]:
                _, idx = heapq.heappop(reservation)
                heapq.heappush(currRooms, idx)

            if len(currRooms) > 0:
                currAvailableRoom = heapq.heappop(currRooms)
                heapq.heappush(reservation, (meetings[i][1], currAvailableRoom))
                counter[currAvailableRoom] += 1                
            elif n > len(reservation):
                currAvailableRoom = len(reservation) 
                heapq.heappush(reservation, (meetings[i][1], currAvailableRoom))
                counter[currAvailableRoom] += 1
            else:
                lastMeetingEndTime, idx = heapq.heappop(reservation)
                currMeetingDuration = meetings[i][1]-meetings[i][0]
                heapq.heappush(reservation, (max(meetings[i][0], lastMeetingEndTime)+currMeetingDuration, idx))
                counter[idx] += 1
            
            i += 1

        maxMeetings, resIdx = 0, 0
        for key, val in counter.items():
            if val > maxMeetings:
                maxMeetings = val
                resIdx = key

        return resIdx