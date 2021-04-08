from tips import Tips


class TipsLibrary:
    def __init__(self):
        self._tips = Tips()

    def new_tip(self, author, url):
        self._tips.add_tip(author, url)
