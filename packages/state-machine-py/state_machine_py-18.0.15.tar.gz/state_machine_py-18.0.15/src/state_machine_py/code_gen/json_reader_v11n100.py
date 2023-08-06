import json
from collections import OrderedDict


class JsonReaderV11n100:
    @classmethod
    def read_file(clazz, file_path):

        # JSON形式のファイルを読込みます
        with open(file_path, encoding="utf-8") as f:
            in_text = f.read()
            # print(f"in_text={in_text}")

        doc = json.loads(in_text, object_pairs_hook=OrderedDict)
        # print(f"doc={doc}")

        return doc
