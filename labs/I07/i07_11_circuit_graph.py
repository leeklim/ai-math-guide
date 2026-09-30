from __future__ import annotations

from collections import defaultdict, deque

from labs.I07.common import emit


def run() -> dict[str, object]:
    nodes = ["input", "copy_head", "mlp_gate", "logit"]
    edges = [("input", "copy_head"), ("input", "mlp_gate"), ("copy_head", "logit"), ("mlp_gate", "logit")]
    indegree = {node: 0 for node in nodes}
    outgoing: dict[str, list[str]] = defaultdict(list)
    for source, target in edges:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = deque(node for node in nodes if indegree[node] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for target in outgoing[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return {
        "nodes": nodes,
        "edges": [list(edge) for edge in edges],
        "topological_order": order,
        "is_acyclic": len(order) == len(nodes),
        "behavior_metric": "target-minus-foil logit",
    }


if __name__ == "__main__":
    emit(run())
