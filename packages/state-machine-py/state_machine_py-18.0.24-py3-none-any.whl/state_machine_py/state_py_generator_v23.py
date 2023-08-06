import sys
import argparse
import traceback

from state_machine_py.main_finally import MainFinally
from state_machine_py.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100
from state_machine_py.code_gen.state_files_gen_v18 import gen_state_files_v18


class Main:
    """状態を定義した .pyファイルを作成します

    Examples
    --------
    # Windows
    python.exe -m lesson23.state_py_generator_v23 "lesson23_projects/house3n2/conf.toml" "const_file" "transition_file" "const" "output_states_dir"
    #                                             -------------------------------------- ------------ ----------------- ------- -------------------
    #                                             1.                                     2.           3.                4.      5.
    # 1. 設定ファイル（TOML形式）へのパス
    # 2. 定数を定義した入力ファイル（JSON形式）へのパスが入ったプロパティの名前
    # 3. 状態遷移を定義した入力ファイル（JSON形式）へのパスが入ったプロパティの名前
    # 4. [import_module]テーブル下の、import文のモジュールへのパスが入ったプロパティの名前
    # 5. 状態ファイル出力ディレクトリーパスのプロパティ名

    # Example: conf.toml
    # 定数
    const_file = "lesson18n2_projects/house3/data/const.json"

    # 状態遷移
    transition_file = "lesson20_projects/house3n2/auto_gen/data/transition3.json"

    # 状態ファイル出力ディレクトリー
    output_states_dir = "lesson23_projects/house3n2/auto_gen/code/states"

    [import_module]
    const = "lesson23_projects.house3n2.auto_gen.data.const"
    """

    def on_main(self):
        parser = argparse.ArgumentParser(description='ステートを定義した .pyファイルを作成します')
        parser.add_argument('conf',
                            help='設定ファイル（TOML形式）へのパス')
        parser.add_argument('const',
                            help='定数を定義した入力ファイル（JSON形式）へのパスが入ったプロパティの名前')
        parser.add_argument('transition',
                            help='状態遷移を定義した入力ファイル（JSON形式）へのパスが入ったプロパティの名前')
        parser.add_argument('import_module',
                            help='[import_module]テーブル下の、import文のモジュールへのパスが入ったプロパティの名前')
        parser.add_argument('output',
                            help='状態を定義したファイルを出力するディレクトリ')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        const_file_path = toml_doc[args.const]
        transition_file_path = toml_doc[args.transition]
        import_module_path = toml_doc['import_module'][args.import_module]
        output_graph_text_file = toml_doc[args.output]

        # JSONファイルから、定数と遷移の設定を読込みます
        const_json_obj = JsonReaderV11n100.read_file(const_file_path)
        transition_doc = JsonReaderV11n100.read_file(transition_file_path)

        # 状態の .py スクリプトを出力します
        gen_state_files_v18(
            dir_path=output_graph_text_file,
            const_doc=const_json_obj,
            transition_doc=transition_doc,
            import_from_path=import_module_path,
        )
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
