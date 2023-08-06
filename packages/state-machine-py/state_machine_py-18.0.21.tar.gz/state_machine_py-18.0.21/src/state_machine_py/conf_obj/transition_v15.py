class TransitionV15:
    """あとで機能拡張するベースになります"""

    def __init__(self, doc):
        self._doc = doc

    @property
    def doc(self):
        """ドキュメント構造のルート"""
        return self._doc
