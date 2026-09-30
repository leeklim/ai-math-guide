from __future__ import annotations

from labs.I07.common import emit


def answer(hidden_signal: int, rationale_signal: int, uses_rationale: bool) -> int:
    return rationale_signal if uses_rationale else hidden_signal


def run() -> dict[str, object]:
    hidden_signal = 1
    original_rationale = 1
    perturbed_rationale = 0
    faithful_original = answer(hidden_signal, original_rationale, True)
    faithful_perturbed = answer(hidden_signal, perturbed_rationale, True)
    post_hoc_original = answer(hidden_signal, original_rationale, False)
    post_hoc_perturbed = answer(hidden_signal, perturbed_rationale, False)
    return {
        "faithful_model_answer_change": faithful_original != faithful_perturbed,
        "post_hoc_model_answer_change": post_hoc_original != post_hoc_perturbed,
        "same_original_rationale_text_can_have_different_dependency": True,
        "evaluated_property": "causal dependence on rationale intervention",
    }


if __name__ == "__main__":
    emit(run())
