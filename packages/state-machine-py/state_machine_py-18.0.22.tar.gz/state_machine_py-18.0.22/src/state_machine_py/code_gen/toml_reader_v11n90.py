from tomlkit import parse


class TomlReaderV11n90:
    @classmethod
    def read_file(clazz, file_path):

        # テキストファイルを読込みます
        with open(file_path, encoding="utf-8") as f:
            text = f.read()

        # TOML形式のテキストをパースします
        return parse(text)
