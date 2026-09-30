from __future__ import annotations

from labs.I07.common import emit


def graph(a: float, edge_a_to_b: float | None = None, node_a: float | None = None) -> dict[str, float]:
    a_value = a if node_a is None else node_a
    message_to_b = a_value if edge_a_to_b is None else edge_a_to_b
    c = 2.0 * a_value
    b = 3.0 * message_to_b + 5.0 * c
    return {"a": a_value, "c": c, "b": b}


def run() -> dict[str, object]:
    clean = graph(2.0)
    corrupt = graph(-1.0)
    edge_patched = graph(-1.0, edge_a_to_b=clean["a"])
    node_patched = graph(-1.0, node_a=clean["a"])
    return {
        "clean_output": clean["b"],
        "corrupt_output": corrupt["b"],
        "edge_patch_output": edge_patched["b"],
        "node_patch_output": node_patched["b"],
        "edge_effect": edge_patched["b"] - corrupt["b"],
        "total_node_effect": node_patched["b"] - corrupt["b"],
    }


if __name__ == "__main__":
    emit(run())
