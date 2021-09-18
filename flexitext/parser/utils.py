class StylesQueue:
    def __init__(self):
        self.styles = {}

    def add(self, styles):
        for name, value in styles.items():
            if name in self.styles:
                self.styles[name].append(value)
            else:
                self.styles[name] = [value]

    def remove(self, names):
        for name in names:
            self.styles[name].pop(-1)
            if not self.styles[name]:
                self.styles.pop(name)

    def get_current(self):
        return {name: value[-1] for name, value in self.styles.items()}
