class InfList(list):
    """Infinite list container"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._index = 0

    def current(self):
        return self[self._index]

    def next(self):
        self._index = (self._index + 1) % len(self)
        return self[self._index]

    def prev(self):
        self._index = (self._index - 1) % len(self)
        return self[self._index]
