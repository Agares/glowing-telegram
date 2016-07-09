from blocks.externalip import ExternalIp
from blocks.freediskspace import FreeDiskSpace
from blocks.pulseaudio import PulseAudio
from blocks.mpdblock import MpdBlock
from blocks.networkinterface import NetworkInterface
from blocks.systemload import SystemLoad
from blocks.power import Power
from blocks.systemtime import SystemTime

blocks = [
    PulseAudio(),
    MpdBlock(),
    FreeDiskSpace(),
    FreeDiskSpace("/media/hdd"),
    NetworkInterface("wlp6s0"),
    ExternalIp(),
    SystemLoad(),
    Power(),
    SystemTime()
]
