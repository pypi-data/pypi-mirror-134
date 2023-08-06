class ClusteredDirectiveEdgeV15:
    """エッジがどのクラスターに所属するかという観点で分類したもの"""

    @classmethod
    def clustering(clazz, directive_edge):
        src = directive_edge.src  # List
        dst = directive_edge.dst
        cluster = []

        if (src is None) or (dst is None):
            min_n = 0
        else:
            min_n = min(len(src), len(dst))

        # 一致するところまでが、同じクラスター
        for i in range(0, min_n):
            if src[i] == dst[i]:
                cluster.append(src[i])
            else:
                break

        return ClusteredDirectiveEdgeV15(directive_edge, cluster)

    def __init__(self, directive_edge, cluster):
        self._directive_edge = directive_edge
        self._cluster = cluster

    def __str__(self):
        cluster_str = "/".join(self._cluster)
        return f"[{cluster_str}]--{self._directive_edge.name}-->"

    @property
    def directive_edge(self):
        return self._directive_edge

    @property
    def cluster(self):
        return self._cluster

    def to_cluster_str(self):
        return "/".join(self._cluster)
