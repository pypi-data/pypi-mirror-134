import json
from collections import OrderedDict


class JsonReaderV17n2:
    @classmethod
    def read_file(clazz, file_path):

        # Pivotファイル（JSON形式）を読込みます
        with open(file_path, encoding="utf-8") as f:
            in_text = f.read()
            # print(f"in_text={in_text}")

        transition_conf_data = json.loads(in_text, object_pairs_hook=OrderedDict)
        # print(f"transition_conf_data={transition_conf_data}")

        return transition_conf_data
