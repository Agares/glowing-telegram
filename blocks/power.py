import colors
import icons
from blockcontent import BlockContent


class BatteryStatus:
    def __init__(self):
        pass

    CHARGING = 0
    DISCHARGING = 1
    FULL = 2


class Power:
    def __init__(self, battery="BAT0", adapter="AC"):
        self.adapter = adapter
        self.battery = battery
        self.battery_status = BatteryStatus.FULL
        self.charge = 0.0
        self.animation_step = 0

        self.update()

    def update(self):
        with open("/sys/class/power_supply/" + self.battery + "/status") as status_file:
            status = status_file.read()

            if status == "Full":
                self.battery_status = BatteryStatus.FULL
            elif status == "Discharging":
                self.battery_status = BatteryStatus.DISCHARGING
            elif status == "Charging":
                self.battery_status = BatteryStatus.CHARGING
                self.animation_step = (self.animation_step + 1) % len(icons.BATTERY)

        with open("/sys/class/power_supply/" + self.battery + "/charge_full") as full_charge_file:
            with open("/sys/class/power_supply/" + self.battery + "/charge_now") as current_charge_file:
                self.charge = float(current_charge_file.read()) / float(full_charge_file.read())

    def full_text(self):
        content = BlockContent()

        if self.battery_status == BatteryStatus.FULL:
            content.append_icon(icons.BATTERY[len(icons.BATTERY) - 1])
        elif self.battery_status == BatteryStatus.CHARGING:
            content.append_icon(icons.BATTERY[self.animation_step])
        else:
            icon_index = round(self.charge * (len(icons.BATTERY) - 1), 0)
            content.append_icon(icons.BATTERY[icon_index])

        content.append_text("  ")

        if self.battery_status == BatteryStatus.FULL:
            content.append_text("100%")
        else:
            content.append_text("{0:.0f}".format(self.charge * 100))

        return content

    def color(self):
        return colors.NORMAL