from battery.batterystate import BatteryStatus, BatteryState


class BatteryStateReader(object):
    def __init__(self, battery_id="BAT0"):
        self.__battery_id = battery_id

    def read_state(self):
        status = BatteryStatus.DISCHARGING

        with open("/sys/class/power_supply/" + self.__battery_id + "/status") as status_file:
            raw_status = status_file.read().strip("\n")

            if raw_status == "Full":
                status = BatteryStatus.FULL
            elif raw_status == "Discharging":
                status = BatteryStatus.DISCHARGING
            elif raw_status == "Charging":
                status = BatteryStatus.CHARGING
            else:
                raise NotImplementedError

        with open("/sys/class/power_supply/" + self.__battery_id + "/charge_full") as full_charge_file:
            with open("/sys/class/power_supply/" + self.__battery_id + "/charge_now") as current_charge_file:
                charge = float(current_charge_file.read()) / float(full_charge_file.read())

        return BatteryState(charge, status)
