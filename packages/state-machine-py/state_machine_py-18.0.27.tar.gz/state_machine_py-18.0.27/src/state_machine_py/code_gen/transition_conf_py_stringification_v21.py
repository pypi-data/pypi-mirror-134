from state_machine_py.code_gen.py_syntax.import_gen_v18 import ImportGenV18
from state_machine_py.code_gen.const_conf_v18 import ConstConfV18


class TransitionConfPyStringification:
    def __init__(self, const_py_dict, import_from_path):
        self._const_conf = ConstConfV18(const_py_dict)
        self._used_const_set = set()
        self._import_from_path = import_from_path

    @classmethod
    def n4sp(clazz, indent):
        return "".join(["    "] * indent)  # 4 spaces

    def stringify(self, variable_name, ordered_dict_data):
        """
        Parameters
        ----------
        data :
            OrderedDict を使った構造
        """

        indent = 0
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces
        title = ordered_dict_data["title"]  # TODO ダブルクォーテーションのエスケープ

        # 定数 or "文字列" 判定
        entry_state = ordered_dict_data["entry_state"]
        entry_state = self._const_conf.replace_item(
            entry_state, '"')  # 定数、でなければ "文字列"
        self._const_conf.pickup_from_item_to_set(
            entry_state, self._used_const_set)

        text = f"""{variable_name} = {{
    "title": "{title}",
    "entry_state": {entry_state},
    "data": {{
"""
        indent += 2
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces

        block_list = []
        for key, value in ordered_dict_data["data"].items():
            # 定数 or "文字列" 判定
            k_operand = self._const_conf.replace_item(
                key, '"')  # 定数、でなければ "文字列"
            self._const_conf.pickup_from_item_to_set(
                k_operand, self._used_const_set)

            if isinstance(value, dict):
                block_list.append(
                    f"{n4sp}{k_operand}: {{\n"
                    + f",\n".join(self._child_dict(value, indent + 1))
                    + f"\n{n4sp}}}"
                )
            elif isinstance(value, list):
                block_list.append(
                    f"{n4sp}{k_operand}: [" +
                    ", ".join(self._child_list(value)) + f"]"
                )
            elif value is None:
                block_list.append(f"{n4sp}{k_operand}:null")
            else:
                block_list.append(f"<★Error key={k_operand} value={value}>")

        text += ",\n".join(block_list)

        text += """
    }
}
"""

        # 定数のインポートをファイルの冒頭に付けます
        if 0 < len(self._used_const_set):
            import_statement = ImportGenV18.generate_import(
                from_s=self._import_from_path,
                import_set=self._used_const_set,
            )
            text = f"{import_statement}\n{text}"

        return text

    def _child_dict(self, ordered_dict_data, indent):
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces

        block_list = []
        for k, v in ordered_dict_data.items():
            text = ""

            # 定数 or "文字列" 判定
            k_operand = self._const_conf.replace_item(k, '"')  # 定数、でなければ "文字列"
            self._const_conf.pickup_from_item_to_set(
                k_operand, self._used_const_set)

            text += f"{n4sp}{k_operand}: "

            # v
            if isinstance(v, dict):
                text += (
                    "{\n" + ",\n".join(self._child_dict(v,
                                       indent + 1)) + f"\n{n4sp}}}"
                )
            elif isinstance(v, list):
                text += "[" + ", ".join(self._child_list(v)) + f"]"
            elif v is None:
                text += "None"
            else:
                text += "<★Error>"

            block_list.append(text)
        return block_list

    def _child_list(self, data):
        item_list = []
        for item in data:

            # 定数 or "文字列" 判定
            operand = self._const_conf.replace_item(
                item, '"')  # 定数、でなければ "文字列"
            self._const_conf.pickup_from_item_to_set(
                operand, self._used_const_set)

            item_list.append(operand)
        return item_list
