import sys
import os
import argparse

from state_machine_py.main_finally import MainFinally
from state_machine_py.code_gen.file_io_v16 import FileIo
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100
from state_machine_py.code_gen.transition_conf_py_stringification_v21 import (
    TransitionConfPyStringification,
)


class Main:
    """v21"""

    def on_main(self):
        parser = argparse.ArgumentParser(
            description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input_const', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('input_transition', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('var_name', help='状態遷移ディクショナリーの変数名')
        args = parser.parse_args()

        const_data = JsonReaderV11n100.read_file(args.input_const)
        transition_data = JsonReaderV11n100.read_file(args.input_transition)

        transition_conf_py_stringification = TransitionConfPyStringification(
            const_py_dict=const_data,
            import_from_path=args.import_module,
        )
        out_text = transition_conf_py_stringification.stringify(
            variable_name=args.var_name, ordered_dict_data=transition_data
        )

        FileIo.makedirs(os.path.dirname(args.output))
        print(f"[L21] write {args.output}")
        FileIo.write(args.output, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
