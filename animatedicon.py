class AnimatedIcon(object):
    def __init__(self, icons):
        assert len(icons) > 0

        self.icons = icons
        self.step = 0

    def update(self):
        self.step = (self.step + 1) % len(self.icons)

    def __unicode__(self):
        return self.icons[self.step]
