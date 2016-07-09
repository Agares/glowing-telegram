import colors


class BlockContent:
    def __init__(self):
        self.content = u""

    def append_icon(self, icon, color=colors.ICON):
        self.append_text(icon, color)

    def append_text(self, text, color=colors.NORMAL):
        self.content += u"<span foreground=\"{0}\">{1}</span>".format(color, text)

    def __unicode__(self):
        return self.content
