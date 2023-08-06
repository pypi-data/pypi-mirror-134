import os

from state_machine_py.code_gen.file_io_v11n80 import FileIoV11n80
from state_machine_py.conf_obj.transition_v16n3 import TransitionV16n3
from state_machine_py.code_gen.py_syntax.class_gen_v18 import ClassGenV18
from state_machine_py.code_gen.py_syntax.import_gen_v18 import ImportGenV18
from state_machine_py.code_gen.py_syntax.method_gen_v18 import MethodGenV18
from state_machine_py.code_gen.py_syntax.switch_gen_v16n3 import SwitchGenV16n3


class StateFileGen:
    @classmethod
    def generate_state_file_v18(
        clazz,
        const,
        transition,
        node_path,
        import_module_path,
        output_dir_path,
    ):
        """状態ファイルを作ります。

        Parameters
        ----------
        node_path : str
            "ThisIs/A/ColorPen" のような書式の文字列です
        """

        # 1. Rename 'ThisIs/A/ColorPen' to 'thisis_a_colorpen'
        # 2. Rename 'ThisIs/A/ColorPen' to 'ThisisAColorpen'
        file_stem = StateFileGen.__create_file_stem(node_path)    # 1.
        class_name = StateFileGen.__create_class_name(node_path)  # 2.
        file_path = os.path.join(output_dir_path, f"{file_stem}.py")

        # エッジの分岐部分を生成
        directed_edge_list = TransitionV16n3.create_edge_list_by_node_path(
            transition.doc['data'], node_path.split("/")
        )

        # 使った定数を set に集めます
        used_const_set = set()
        for edge in directed_edge_list:
            const.pickup_from_item_to_set(edge.name, used_const_set)

        class_name_line = ClassGenV18.generate_class(
            name=f"{class_name}State")
        method_signature_line = MethodGenV18.signature(
            name="update",
            parameters_s="self, req")
        method_body = """
        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
"""

        # エッジ分岐部
        used_const_set = set()  # 使った定数
        switch_model = StateFileGen.__edge_switch_model(
            const=const,
            directed_edge_list=directed_edge_list,
            used_const_set=used_const_set,
        )
        switch_block = SwitchGenV16n3.generate_switch(indent="        ",
                                                      switch_model=switch_model)
        # ハンドラ生成
        on_entry_block = MethodGenV18.generate_method(name="on_entry",
                                                      parameters_s="self, req")
        on_trigger_block = MethodGenV18.generate_method(
            name="on_trigger",
            parameters_s="self, req",
            body_sequence=["return req.context.pull_trigger()"])

        on_some_handler_block = ""
        # ハンドラ自動生成
        for edge in directed_edge_list:
            if edge.name != "":
                on_some_handler_block += MethodGenV18.generate_method(
                    name=f"on_{edge.name}", parameters_s="self, req"
                )

        # 定数のインポート文
        if 0 < len(used_const_set):
            import_statement = ImportGenV18.generate_import(
                from_s=import_module_path,
                import_set=used_const_set,
            )
            import_statement += "\n"
        else:
            import_statement = ""

        text = ""
        text += import_statement
        text += class_name_line
        text += method_signature_line
        text += method_body
        text += switch_block
        text += "\n"
        text += on_entry_block
        text += on_trigger_block
        text += on_some_handler_block

        FileIoV11n80.write(file_path, text)

    @classmethod
    def __edge_switch_model(clazz, const, directed_edge_list, used_const_set):
        """エッジ分岐部"""

        if_elif_list = []
        # if～elif文のコード部分
        # +------------------------+
        # | if msg == xx1xx:       | 1. edge_operand
        # |     self.on_xx2xx(req) | 2. edge.name
        # |     return xx1xx       |
        # +------------------------+
        for edge in directed_edge_list:

            # エッジ名を定数に置きかえれるか試します
            edge_operand = const.replace_item(
                edge.name, '"')  # 定数、でなければ "文字列"

            # 条件式
            if edge.name == "":
                cond = "True"  # 恒真
            else:
                # この練習プログラムでは E_XXX のような定数になってるはず
                const.pickup_from_item_to_set(
                    edge_operand, used_const_set)
                cond = f"msg == {edge_operand}"

            # 本文シーケンス
            body_sequence = []
            body_sequence.append(f"self.on_{edge.name}(req)")  # イベントハンドラ呼出し
            # エッジ名を返します
            body_sequence.append(f"return {edge_operand}")

            if_elif_list.append([cond, body_sequence])

        # None のケースを追加（ステートマシンの終了）
        if_elif_list.append(["msg == None", ["return None"]])

        # else文のコード部分
        # +-----------------------------------------------+
        # | else:                                         |
        # |     raise ValueError(f"Unexpected msg:{msg}") |
        # +-----------------------------------------------+
        else_sequence = ['raise ValueError(f"Unexpected msg:{msg}")']

        switch_model = [if_elif_list, else_sequence]
        return switch_model

    @classmethod
    def __create_file_stem(clazz, node_path):
        """ 'ThisIs/A/ColorPen' であれば、 'thisis_a_colorpen' に変換します"""
        return node_path.replace("/", "_").lower()

    @classmethod
    def __create_class_name(clazz, node_path):
        """ 'ThisIs/A/ColorPen' であれば、 'ThisisAColorpen' に変換します """
        class_name = ""
        for node in node_path.split("/"):
            node = node.capitalize()
            class_name += node
        return class_name
