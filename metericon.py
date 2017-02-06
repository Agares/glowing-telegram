class MeterIcon(object):
    def __init__(self, icons):
        assert len(icons) > 0
        self.__icons = icons
        self.__state = 0.0

    def update(self, state):
        self.__state = state

    def __unicode__(self):
        icon_index = (len(self.__icons) - 1) * self.__state
        icon_index = round(icon_index)
        icon_index = int(icon_index)
        
        if icon_index >= len(self.__icons):
            icon_index -= 1

        return self.__icons[icon_index]
