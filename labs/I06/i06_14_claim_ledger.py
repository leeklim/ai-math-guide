from __future__ import annotations

from labs.I06.common import emit


CLAIM_LEVELS = ["observed", "recoverable", "used", "causal", "generalized"]


def allowed_claim(evidence: dict[str, bool]) -> str:
    level = "observed"
    if evidence["held_out_probe"] and evidence["control_passed"]:
        level = "recoverable"
    if evidence["functional_test"]:
        level = "used"
    if evidence["controlled_intervention"]:
        level = "causal"
    if evidence["replicated_across_settings"] and level == "causal":
        level = "generalized"
    return level


def run() -> dict[str, object]:
    evidence = {
        "activation_difference": True,
        "held_out_probe": True,
        "control_passed": True,
        "functional_test": False,
        "controlled_intervention": False,
        "replicated_across_settings": False,
    }
    claim = allowed_claim(evidence)
    return {"evidence": evidence, "allowed_claim": claim, "claim_rank": CLAIM_LEVELS.index(claim)}


if __name__ == "__main__":
    emit(run())
