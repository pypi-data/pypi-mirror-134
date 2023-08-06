from graphviz import Digraph

from state_machine_py.conf_obj.clustered_directive_edge_v15 import ClusteredDirectiveEdgeV15
from state_machine_py.graph_gen.render_v15 import create_edge_list_v15


def clustering(edge_list):
    """ノードパスによってクラスタリング"""
    clustered_edge_in_list = []

    for edge in edge_list:
        clustering_edge = ClusteredDirectiveEdgeV15.clustering(edge)
        clustered_edge_in_list.append(clustering_edge)

    return clustered_edge_in_list


def rearrenge_in_tree(clustered_edge_in_list):
    """ツリー構造に再配置"""
    tree = {}

    for clustering_edge in clustered_edge_in_list:
        print("----")
        print(
            f"clustering_edge.directive_edge={clustering_edge.directive_edge}")

        print(
            f"clustering_edge.to_cluster_str()={clustering_edge.to_cluster_str()}")

        curr_dict = tree

        if len(clustering_edge.cluster) < 1:
            print(
                f"len(clustering_edge.cluster)={len(clustering_edge.cluster)}")
            pass
        else:

            for cluster_node in clustering_edge.cluster:
                print(f"  cluster_node={cluster_node}")

                if not (cluster_node in curr_dict):
                    curr_dict[cluster_node] = {}

                curr_dict = curr_dict[cluster_node]

        if "__edge__" in curr_dict:
            curr_dict["__edge__"].append(clustering_edge.directive_edge)
        else:
            curr_dict["__edge__"] = [clustering_edge.directive_edge]

    print("----")
    return tree


class GraphRenderV15n2:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        # グラフの設定
        self._g = Digraph(format="png")
        self._g.attr("node", shape="square", style="filled")

    def write(self, transition, output_text_file):

        edge_list = []

        # エッジの一覧を作成
        create_edge_list_v15(transition.doc['data'], [], None, edge_list)

        # ノードパスによってクラスタリング
        clustered_edge_in_list = clustering(edge_list)
        # Debug
        for clustering_edge in clustered_edge_in_list:
            print(f"clustering_edge={clustering_edge}")

        # ツリー構造に再配置
        tree = rearrenge_in_tree(clustered_edge_in_list)
        # Debug

        def __show_tree(curr_dict, indent, cluster_name):
            # エッジを先に検出
            if "__edge__" in curr_dict:
                edge_list = curr_dict["__edge__"]
                for edge in edge_list:
                    print(f"[Tree] {indent}{cluster_name} value={edge}")

            for key, value in curr_dict.items():
                if key == "__edge__":
                    pass  # 検出済み
                else:
                    __show_tree(value, f"{indent}  ", f"cluster_{key}")

        __show_tree(tree, "", "cluster_root")

        # クラスター 'cluster_' から名前を始める必要あり
        with self._g.subgraph(name="cluster_root") as c:
            # 一番外側のクラスターのラベルは図のタイトルのように見える
            c.attr(color="white", label=transition.doc['title'])
            # 始端記号
            c.node("(Start)", shape="circle", color="gray")
            # 始端と開始ノードのエッジ
            c.edge(
                "(Start)", transition.doc['entry_state'], label="start")
            # 終端記号
            c.node("(Terminal)", shape="circle", color="gray")

            # Debug
            def __create_cluster(curr_dict, indent, cluster_key):
                with self._g.subgraph(name=f"cluster_{cluster_key}") as c2:
                    c2.attr(color="pink", label=cluster_key)

                    # エッジを先に検出
                    if "__edge__" in curr_dict:
                        edge_list = curr_dict["__edge__"]
                        for edge in edge_list:
                            src_node = edge.to_src_str()
                            dst_node = edge.to_dst_str()
                            if dst_node is None:
                                dst_node = "(Terminal)"
                            # ノード
                            c2.node(src_node, shape="circle", color="pink")
                            # エッジ
                            c2.edge(src_node, dst_node, label=edge.name)

                    for key, value in curr_dict.items():
                        if key == "__edge__":
                            pass  # 検出済み
                        else:
                            __create_cluster(value, f"{indent}  ", key)

            __create_cluster(tree, "", "root")

        # 描画
        self._g.render(output_text_file)

    def clean_up(self):
        pass
