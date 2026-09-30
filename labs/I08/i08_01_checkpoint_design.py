from __future__ import annotations

from labs.I08.common import emit


def run() -> dict[str, object]:
    checkpoints = [0, 1_000, 10_000, 50_000, 100_000, 143_000]
    contract = {
        "repository": "EleutherAI/pythia-160m-deduped",
        "revisions": [f"step{step}" for step in checkpoints],
        "data": "eight fixed prompts: four place and four animal prompts",
        "seed": 20261001,
        "layer": 5,
        "token": "last",
        "metrics": ["target first-token NLL", "condition probe accuracy", "zero-ablation margin change"],
    }
    return {"checkpoint_count": len(checkpoints), "strictly_increasing": checkpoints == sorted(set(checkpoints)), "contract": contract}


if __name__ == "__main__":
    emit(run())
