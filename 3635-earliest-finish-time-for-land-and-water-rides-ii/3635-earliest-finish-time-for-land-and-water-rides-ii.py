class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(startingRide, startingRideDuration, endingRide, endingRideDuration):
            startingRideMax = inf
            for i,time in enumerate(startingRide):
                startingRideMax = min(startingRideMax, time + startingRideDuration[i])
            endingRideMax = inf
  
            for i,time in enumerate(endingRide):
                if time < startingRideMax:
                    endingRideMax = min(endingRideMax, startingRideMax + endingRideDuration[i])
                else:
                    endingRideMax = min(endingRideMax, time + endingRideDuration[i])
            print(endingRideMax)
            return endingRideMax
        return min(solve(landStartTime, landDuration, waterStartTime, waterDuration),solve(waterStartTime, waterDuration, landStartTime, landDuration))