class MethodGen:
    @classmethod
    def generate_method(clazz, name, parameters_s, body_sequence=None):
        signature = MethodGen.signature(name=name, parameters_s=parameters_s)

        if body_sequence is None:
            body = "        pass\n\n"
        else:
            body = "        " + "\n".join(body_sequence) + "\n\n"

        return "".join([signature, body])

    @classmethod
    def signature(clazz, name, parameters_s):
        return f"    def {name}({parameters_s}):\n"
