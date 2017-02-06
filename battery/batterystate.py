class BatteryStatus(object):
    CHARGING = 0
    DISCHARGING = 1
    FULL = 2
    UNKNOWN = 3


class BatteryState(object):
    def __init__(self, charge, status):
        self.__charge = charge
        self.__status = status

    def charge(self):
        return self.__charge

    def status(self):
        return self.__status
