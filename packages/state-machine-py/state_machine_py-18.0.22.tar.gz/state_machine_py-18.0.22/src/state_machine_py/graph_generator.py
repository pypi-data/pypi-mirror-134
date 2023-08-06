import sys
import argparse
import traceback

from state_machine_py.main_finally import MainFinally
from state_machine_py.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100
from state_machine_py.conf_obj.transition_v15 import TransitionV15
from state_machine_py.graph_gen.render_v15n2 import GraphRenderV15n2


class Main:
    """設定ファイル（.toml）を指定することで、状態遷移図を出力します。

    # コマンド
    python.exe -m this.is.a.module.graph_generator "this/is/a/path/conf.toml"

    設定ファイルに必要な内容は以下の通りです。

    # 状態遷移図
    transition_file = "This/is/a/path/transition.json"

    # 状態遷移図の出力先
    output_graph_text_file = "This/is/a/path/transigion_graph.txt"
    """

    def __init__(self):
        self._graph_render = None

    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc['transition_file']
        output_graph_text_file = toml_doc['output_graph_text_file']

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # オブジェクト作成
        transition = TransitionV15(transition_doc)

        # グラフ描画
        self._graph_render = GraphRenderV15n2()
        self._graph_render.write(
            transition=transition,
            output_text_file=output_graph_text_file)
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if self._graph_render:
            self._graph_render.clean_up()

        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
