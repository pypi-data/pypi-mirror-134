from state_machine_py.conf_obj.transition_v15 import TransitionV15
from state_machine_py.conf_obj.directive_edge_v15 import DirectiveEdgeV15


class TransitionV16n2(TransitionV15):
    def create_edge_list(self):
        """辺（DirectiveEdgeクラス）の一覧を作成"""

        def __create_edge_list(
            curr_dict, parent_state_node_path, node_name, result_edge_list
        ):
            state_node_path = list(parent_state_node_path)
            if not (node_name is None) and not (node_name is ""):
                state_node_path.append(node_name)

            print(
                f"parent_state_node_path={parent_state_node_path} node_name={node_name} state_node_path={state_node_path}"
            )

            for child_key in curr_dict.keys():

                child = curr_dict[child_key]

                if isinstance(child, dict):
                    __create_edge_list(
                        child, state_node_path, child_key, result_edge_list
                    )
                else:
                    edge = DirectiveEdgeV15(
                        src=state_node_path, dst=child, name=child_key)
                    result_edge_list.append(edge)

        result_edge_list = []

        __create_edge_list(self._data, [], "", result_edge_list)

        return result_edge_list

    @classmethod
    def extract_node_path_set(clazz, edge_list):
        """エッジにノードパスが含まれているので、エッジを元にノードパス文字列のセットを作成します"""
        node_path_set = set()

        for edge in edge_list:
            node_path_set.add(edge.to_src_str())
            node_path_set.add(edge.to_dst_str())

        return node_path_set
