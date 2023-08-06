class TransitionConfV15:
    def __init__(self, data):
        self._title = data["title"]
        self._entry_state = data["entry_state"]
        self._data = data["data"]

    @property
    def title(self):
        """図のタイトル"""
        return self._title

    @property
    def entry_state(self):
        """開始ノードの名前"""
        return self._entry_state

    @property
    def data(self):
        """ツリー構造のエッジ"""
        return self._data
