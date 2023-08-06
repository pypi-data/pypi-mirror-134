from state_machine_py.conf_obj.transition_v15 import TransitionV15
from state_machine_py.graph_gen.render_v15 import create_edge_list_v15


class TransitionV16n2(TransitionV15):
    def create_edge_list_v16n2(self):
        """辺（DirectiveEdgeクラス）の一覧を作成"""

        result_edge_list = []

        create_edge_list_v15(self.doc['data'], [], "", result_edge_list)

        return result_edge_list

    @classmethod
    def extract_node_path_set(clazz, edge_list):
        """エッジにノードパスが含まれているので、エッジを元にノードパス文字列のセットを作成します"""
        node_path_set = set()

        for edge in edge_list:
            node_path_set.add(edge.to_src_str())
            node_path_set.add(edge.to_dst_str())

        return node_path_set
