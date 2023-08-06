class ConstConfV18:
    def __init__(self, data):
        # (1) キーと値は 全単射にしてください
        # (2) 大文字と小文字は区別します
        self._data = data

        # 逆向きは自動生成します
        self._rev_data = {}

        init_size = len(self._data)

        for key, value in self._data.items():
            if value in self._rev_data:
                raise ValueError(f"value:{value} が重複しました。全単射にしてください")

            self._rev_data[value] = key

        if init_size != len(self._rev_data):
            raise ValueError("定数のキーとバリューは全単射にしてください")

    @property
    def data(self):
        return self._data

    @property
    def rev_data(self):
        return self._rev_data

    def replace_item(self, item, quote):
        """文字列に対して、定数に書きかえられるなら定数に書きかえて返します"""
        if item in self.rev_data:
            return self.rev_data[item]  # 定数
        else:
            return f"{quote}{item}{quote}"  # 文字列

    def replace_list(self, old_list, quote):
        """リストに対して、定数に書きかえられる要素は定数に書きかえた新しいリストを返します"""
        new_list = []
        for item in old_list:
            if item in self._rev_data:
                new_list.append(self._rev_data[item])  # 定数
            else:
                new_list.append(f"{quote}{item}{quote}")  # 文字列

        return new_list

    def pickup_from_item_to_set(self, item, used_const_set):
        """item が定数なら used_const_set へ追加します"""
        if item in self._data:
            used_const_set.add(item)

    def pickup_from_list(self, list_obj, used_const_set):
        """list_obj の中で使われている定数を used_const_set へ追加します"""
        for item in list_obj:
            if item in self._data:
                used_const_set.add(item)
