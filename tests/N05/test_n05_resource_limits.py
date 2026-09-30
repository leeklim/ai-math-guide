from __future__ import annotations

import unittest

import torch

from labs.N05 import (
    n05_01_tensor_graph,
    n05_02_single_neuron,
    n05_03_mlp_forward,
    n05_04_activation_gating,
    n05_05_softmax_cross_entropy,
    n05_06_backpropagation,
    n05_07_minibatch_gradient_descent,
    n05_08_adamw_state,
    n05_09_tensor_shape_dtype,
    n05_10_jvp_vjp,
)
from labs.N05.common import LIMITS, assert_within_limits


class ResourceLimitTest(unittest.TestCase):
    def test_all_pilot_examples_stay_within_limits(self) -> None:
        for module in (
            n05_01_tensor_graph,
            n05_02_single_neuron,
            n05_03_mlp_forward,
            n05_04_activation_gating,
            n05_05_softmax_cross_entropy,
            n05_06_backpropagation,
            n05_07_minibatch_gradient_descent,
            n05_08_adamw_state,
            n05_09_tensor_shape_dtype,
            n05_10_jvp_vjp,
        ):
            with self.subTest(example=module.EXAMPLE_ID):
                assert_within_limits(module.SPEC)

    def test_hard_limits_match_project_specification(self) -> None:
        self.assertEqual(LIMITS.batch_size, 2)
        self.assertEqual(LIMITS.sequence_length, 32)
        self.assertEqual(LIMITS.model_dimension, 64)
        self.assertEqual(LIMITS.transformer_layers, 2)
        self.assertEqual(LIMITS.attention_heads, 4)
        self.assertEqual(LIMITS.vocabulary_size, 256)
        self.assertEqual(LIMITS.parameter_count, 250_000)
        self.assertEqual(LIMITS.training_steps, 50)

    def test_runtime_is_single_threaded_after_an_example(self) -> None:
        n05_01_tensor_graph.compute()
        self.assertEqual(torch.get_num_threads(), 1)
        self.assertEqual(torch.get_num_interop_threads(), 1)


if __name__ == "__main__":
    unittest.main()
