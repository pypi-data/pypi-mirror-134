class ConstV17:
    def __init__(self, doc):
        # (1) キーと値は 全単射にしてください
        # (2) キーも値も 大文字と小文字は区別します
        self._doc = doc

        # 逆向きは自動生成します
        self._rev_data = {}

        init_size = len(self._doc)

        for key, value in self._doc.items():
            if value in self._rev_data:
                raise ValueError(f"value:{value} が重複しました。全単射にしてください")

            self._rev_data[value] = key

        if init_size != len(self._rev_data):
            raise ValueError("定数のキーとバリューは全単射にしてください")

    @property
    def doc(self):
        return self._doc

    @property
    def rev_data(self):
        return self._rev_data

    def stringify(self, value, quote):
        """TODO 文字列化を行います。
        例えば引数 value="Init" であれば、 "Init" というダブルクォーテーション付きの文字列を返します。
        このとき、 INIT = "Init" という定数定義があれば、 INIT という文字列を返します。

        TODO クォートのエスケープをしたい

        Parameters
        ----------
        text : str
            文字列
        quote : str
            " か ' かを選べます
        """

        if value in self._rev_data:
            return self._rev_data[value]

        return f"{quote}{value}{quote}"
