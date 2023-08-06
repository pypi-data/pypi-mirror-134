from state_machine_py.code_gen.const_file_gen_v17 import gen_const_file_v17
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100


def gen_const_py(input_path, output_path):
    """定数を定義したJSONファイルを元に、Pythonスクリプトを出力"""

    # JSON構造（順序付きDict）に変換 --> 出力
    transition_json_obj = JsonReaderV11n100.read_file(input_path)
    gen_const_file_v17(output_path, transition_json_obj)
