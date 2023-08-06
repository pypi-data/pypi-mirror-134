import os
from state_machine_py.code_gen.file_io_v16 import FileIo
from state_machine_py.code_gen.const_stringification_v17 import ConstStringification


def gen_const_file_v17(output_file_path, const_conf_py_dict):
    """Pythonスクリプトファイルを生成します"""

    text = ConstStringification.stringify(const_conf_py_dict)

    # 出力
    FileIo.makedirs(os.path.dirname(output_file_path))
    FileIo.write(output_file_path, text)
