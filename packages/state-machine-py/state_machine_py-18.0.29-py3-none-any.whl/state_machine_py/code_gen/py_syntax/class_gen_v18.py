class ClassGenV18:
    @classmethod
    def generate_class(self, name, super_class_name=""):
        return f"class {name}({super_class_name}):\n"
