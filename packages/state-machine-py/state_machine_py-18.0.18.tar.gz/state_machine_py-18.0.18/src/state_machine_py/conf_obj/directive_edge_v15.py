class DirectiveEdgeV15:
    """向きのある辺"""

    def __init__(self, src, dst, name):
        self._src = src
        self._dst = dst
        self._name = name

    def __str__(self):
        return f"[{self.to_src_str()}]--{self._name}-->[{self.to_dst_str()}]"

    @property
    def name(self):
        """名前"""
        return self._name

    # @name.setter
    # def name(self, val):
    #    self._name = val

    @property
    def src(self):
        """遷移元の状態ノードが縦に並ぶリスト"""
        return self._src

    # @src.setter
    # def path(self, val):
    #    self._src = val

    @property
    def dst(self):
        """遷移先の状態ノードが縦に並ぶリスト"""
        return self._dst

    # @dst.setter
    # def dst(self, val):
    #    self._dst = val

    def to_src_str(self):
        """遷移後ノードパス"""
        return "/".join(self._src)

    def to_dst_str(self):
        """遷移先ノードパス"""
        if self._dst is None:
            return None
        else:
            return "/".join(self._dst)
