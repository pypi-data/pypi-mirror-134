from state_machine_py.code_gen.const_conf_v17 import ConstConfV17


class ConstStringification:
    @classmethod
    def stringify(clazz, const_conf_py_dict):
        const_conf = ConstConfV17(const_conf_py_dict)

        text = ""

        for key, value in const_conf.data.items():
            text += f"{key} = '{value}'\n"

        return text
