class ConstConfV17:
    def __init__(self, data):
        self._data = data

        # 逆向きは自動生成します
        self._rev_data = {}

        for key, value in self._data.items():
            self._rev_data[value] = key

    @property
    def data(self):
        return self._data

    @property
    def rev_data(self):
        return self._rev_data

    def stringify(self, value, quote):
        """文字列化を行います。
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
