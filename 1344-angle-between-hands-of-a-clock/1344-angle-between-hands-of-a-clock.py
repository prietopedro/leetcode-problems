class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ## 360
        # 12 hours (30 between each hour)
        # 60 minutes (6 between each minute)
        ##hour
        prec_hour = ((hour + (1 / (60 / minutes))) % 12) if minutes else hour
        prec_hour *= 30
        prec_hour = prec_hour % 360
        prec_minute = 360 / (60 / minutes) if minutes else minutes
        return min(abs(prec_minute - prec_hour),360 - abs(prec_minute - prec_hour))