import os


class FileIo:
    @classmethod
    def write(clazz, file_path, text):
        with open(file_path, "w", encoding="UTF-8") as f:
            f.write(text)

    @classmethod
    def makedirs(clazz, dir_path):
        """フォルダーが無ければ作ります。既存なら無視します"""
        try:
            # フォルダーが無ければ作る
            os.makedirs(dir_path)
        except FileExistsError:
            # 既存なら無視
            pass
