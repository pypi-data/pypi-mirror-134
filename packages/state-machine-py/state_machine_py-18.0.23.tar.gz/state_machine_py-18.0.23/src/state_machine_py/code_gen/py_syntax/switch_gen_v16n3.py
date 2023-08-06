class SwitchGen:
    @classmethod
    def generate_switch(clazz, indent, switch_model):
        """分岐構造を記述します

        Parameters
        ----------
        switch_model : list
            [0] if～elifブロックのリスト
                ブロックはさらに [0]条件式 [1]本文 に分かれます
            [1] あればelseブロックのシーケンス

        Examples
        --------
        if 1.expression: # a == b
            return 1.destination

        elif 2.expression: # a == b
            return 2.destination

        else:
            raise ValueError("Unexpected condition")
        """

        # if が1回、 elif がn回繰り返し、 raise が1回

        text = ""

        is_first = True

        if_elif_list = switch_model[0]
        for cond_body in if_elif_list:
            cond = cond_body[0]
            if is_first:
                is_first = False
                text += f"{indent}if {cond}:\n"
            else:
                text += f"{indent}elif {cond}:\n"

            body_sequence = cond_body[1]
            for line in body_sequence:
                text += f"{indent}    {line}\n"

            text += "\n"

        if 0 < len(switch_model):
            else_sequence = switch_model[1]
            if else_sequence:
                text += f"{indent}else:\n"
                for line in else_sequence:
                    text += f"{indent}    {line}\n"

        return text
