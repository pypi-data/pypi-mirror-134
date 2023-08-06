import os

from state_machine_py.code_gen.file_io_v16 import FileIo
from state_machine_py.code_gen.transition_conf_v16n3 import TransitionConfV1n3
from state_machine_py.code_gen.py_syntax.class_gen_v18 import ClassGen
from state_machine_py.code_gen.py_syntax.import_gen_v18 import ImportGen
from state_machine_py.code_gen.py_syntax.method_gen_v18 import MethodGen
from state_machine_py.code_gen.py_syntax.switch_gen_v16n3 import SwitchGen


class StateFileGen:
    @classmethod
    def generate_state_file(
        clazz, dir_path, const_conf, transition_conf, node_path, import_from_path
    ):
        """状態ファイルを作ります。

        Parameters
        ----------
        node_path : str
            "ThisIs/A/ColorPen" のような書式の文字列です
        """

        # "ThisIs/A/ColorPen" であれば、 "thisis_a_colorpen" に変換します
        file_stem = node_path.replace("/", "_").lower()

        # "ThisIs/A/ColorPen" であれば、 "ThisisAColorpen" に変換します
        class_name = ""
        for node in node_path.split("/"):
            node = node.capitalize()
            class_name += node

        # print(f"[Render] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        file_path = os.path.join(dir_path, f"{file_stem}.py")

        # エッジの分岐部分
        directed_edge_list = TransitionConfV1n3.create_edge_list_by_node_path(
            transition_conf.data, node_path.split("/")
        )

        # 使った定数を調査
        used_const_set = set()
        for edge in directed_edge_list:
            const_conf.pickup_from_item_to_set(edge.name, used_const_set)

        text = ""
        text += ClassGen.generate_class(name=f"{class_name}State")
        text += MethodGen.signature(name="update", parameters_s="self, req")
        text += """
        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
"""

        # エッジ分岐部
        used_const_set = set()  # 使った定数
        switch_model = StateFileGen.__edge_switch_model(
            const_conf=const_conf,
            directed_edge_list=directed_edge_list,
            used_const_set=used_const_set,
        )
        text += SwitchGen.generate_switch("        ", switch_model=switch_model)
        text += "\n"

        # ハンドラ生成
        text += MethodGen.generate_method(name="on_entry", parameters_s="self, req")
        text += MethodGen.generate_method(
            name="on_trigger",
            parameters_s="self, req",
            body_sequence=["return req.context.pull_trigger()"],
        )
        # ハンドラ自動生成
        for edge in directed_edge_list:
            if edge.name != "":
                text += MethodGen.generate_method(
                    name=f"on_{edge.name}", parameters_s="self, req"
                )

        # 定数のインポートをファイルの冒頭に付けます
        if 0 < len(used_const_set):
            import_statement = ImportGen.generate_import(
                from_s=import_from_path,
                import_set=used_const_set,
            )
            text = f"{import_statement}\n{text}"

        FileIo.write(file_path, text)

    @classmethod
    def __edge_switch_model(clazz, const_conf, directed_edge_list, used_const_set):

        if_elif_list = []
        # if～elif文
        for edge in directed_edge_list:

            # エッジ名を定数に置きかえれるか試します
            edge_operand = const_conf.replace_item(edge.name, '"')  # 定数、でなければ "文字列"

            # 条件式
            if edge.name == "":
                cond = "True"  # 恒真
            else:
                # この練習プログラムでは E_XXX のような定数になってるはず
                const_conf.pickup_from_item_to_set(edge_operand, used_const_set)
                cond = f"msg == {edge_operand}"

            # 本文シーケンス
            body_sequence = []
            body_sequence.append(f"self.on_{edge.name}(req)")  # イベントハンドラ呼出し
            # エッジ名を返します
            body_sequence.append(f"return {edge_operand}")

            if_elif_list.append([cond, body_sequence])

        # else文
        else_sequence = ['raise ValueError(f"Unexpected msg:{msg}")']

        switch_model = [if_elif_list, else_sequence]
        return switch_model
