import dbus

import icons
from blockcontent import BlockContent


class Spotify(object):
    def __init__(self):
        self.__artist = u''
        self.__title = u''
        self.__status = ''
        self.__spotify = None

        try:
            bus = dbus.SessionBus()
            self.__spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
            self.__spotify_properties = dbus.Interface(self.__spotify, 'org.freedesktop.DBus.Properties')
        except dbus.DBusException:
            pass

    def update(self):
        if not self.__spotify:
            return

        props = self.__spotify_properties.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

        self.__artist = unicode(props['xesam:artist'][0])
        self.__title = unicode(props['xesam:title'])

        playback_status = self.__spotify_properties.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
        self.__status = str(playback_status)

    def full_text(self):
        if not self.__title:
            content = BlockContent()
            content.append_icon(icons.STOP)
            return content

        content = BlockContent()
        content.append_icon({
            'Playing': icons.PLAY,
            'Paused': icons.PAUSE,
            'Stopped': icons.STOP
        }[self.__status])
        content.append_text(u"  {} - {}".format(self.__artist, self.__title))

        return content

    def click(self):
        self.__spotify.get_dbus_method("PlayPause", dbus_interface='org.mpris.MediaPlayer2.Player')()
