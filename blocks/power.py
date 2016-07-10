import icons
from animatedicon import AnimatedIcon
from blockcontent import BlockContent
from metericon import MeterIcon
from battery.batterystate import BatteryState, BatteryStatus
from battery.batterystatereader import BatteryStateReader


class Power(object):
    def __init__(self, battery="BAT0"):
        self.__battery_state_reader = BatteryStateReader(battery)
        self.__battery_state = BatteryState(0.0, BatteryStatus)

        self.__charging_animation = AnimatedIcon(icons.BATTERY)
        self.__meter = MeterIcon(icons.BATTERY)

        self.update()

    def update(self):
        self.__battery_state = self.__battery_state_reader.read_state()

        self.__charging_animation.update()
        self.__meter.update(self.__battery_state.charge())

    def full_text(self):
        content = BlockContent()

        self.__render_icon(content)
        self.__render_spacing(content)
        self.__render_charge(content)

        return content

    def __render_spacing(self, content):
        content.append_text("  ")

    def __render_charge(self, content):
        if self.__battery_state.status() == BatteryStatus.FULL:
            content.append_percentage(1)
        else:
            content.append_percentage(self.__battery_state.charge())

    def __render_icon(self, content):
        if self.__battery_state.status() == BatteryStatus.FULL:
            content.append_icon(icons.BATTERY[len(icons.BATTERY) - 1])
        elif self.__battery_state.status() == BatteryStatus.CHARGING:
            content.append_icon(self.__charging_animation)
        else:
            content.append_icon(self.__meter)
