from blocks.Spotify import Spotify
from blocks.externalip import ExternalIp
from blocks.freediskspace import FreeDiskSpace
from blocks.networkinterface import NetworkInterface
from blocks.power import Power
from blocks.pulseaudio import PulseAudio
from blocks.systemload import SystemLoad
from blocks.systemtime import SystemTime

blocks = [
    PulseAudio(0),
    Spotify(),
    FreeDiskSpace(),
#    FreeDiskSpace("/media/hdd"),
    NetworkInterface("eno1"),
    SystemLoad(),
#    Power(),
    SystemTime()
]
