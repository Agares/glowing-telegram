import colors


class BlockContent(object):
    def __init__(self):
        self.content = ""

    def append_icon(self, icon, color=colors.ICON):
        self.append_text(icon, color)

    def append_text(self, text, color=colors.NORMAL):
        self.content += f"<span foreground=\"{color}\">{text}</span>"

    def append_percentage(self, value, format_def="{:3.0f} %"):
        self.append_text(format_def.format(value * 100))

    def __str__(self):
        return self.content
