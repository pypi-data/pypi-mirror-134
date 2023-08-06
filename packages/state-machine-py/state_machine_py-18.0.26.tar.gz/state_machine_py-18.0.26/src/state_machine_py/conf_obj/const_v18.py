from state_machine_py.conf_obj.const_v17 import ConstV17


class ConstV18(ConstV17):
    def __init__(self, doc):
        super().__init__(doc)

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
        if item in self._doc:
            used_const_set.add(item)

    def pickup_from_list(self, listtransition_doc, used_const_set):
        """listtransition_doc の中で使われている定数を used_const_set へ追加します"""
        for item in listtransition_doc:
            if item in self._doc:
                used_const_set.add(item)
