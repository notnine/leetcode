#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
import heapq
from collections import deque

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations = deque(sorted(stations))
        stations_passed = [] # max heap of fuels of the stations we've passed
        stations_used = 0
        travelled = startFuel

        while travelled < target:
            # while the next station is reachable
            while stations and stations[0][0] <= travelled:
                station_pos, station_fuel = stations.popleft()
                heapq.heappush(stations_passed, -station_fuel)
            
            # refuel with the best station and keep going
            if stations_passed:
                refuel = -heapq.heappop(stations_passed)
                travelled += refuel
                stations_used += 1
            else: # cannot refuel
                return -1
        
        return stations_used


            


        # for i in range(target):
        #     if stations and stations[0][0] == i:
        #         heapq.heappush(stations_passed, -stations[0][1])
        #         stations.popleft()

        #     if curr_fuel == 0:
        #         if not stations_passed:
        #             return -1
        #         refuel = -heapq.heappop(stations_passed)
        #         curr_fuel += refuel
        #         stations_used += 1
            
        #     curr_fuel -= 1

        # return stations_used 
# @lc code=end

