class ImportGenV18:
    @classmethod
    def generate_import(self, from_s, import_set):
        if len(import_set) < 1:
            return ""

        list_s = ", ".join(sorted(import_set))
        return f"from {from_s} import {list_s}\n"
