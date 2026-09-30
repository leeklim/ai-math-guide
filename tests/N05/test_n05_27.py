from __future__ import annotations

import unittest

from labs.N05 import n05_27_checkpoint_state as example


class CheckpointStateTest(unittest.TestCase):
    def test_model_state_reloads_exactly(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["model_state_entries"].item(), 12)
        self.assertEqual(tensors["parameter_entries"].item(), 12)
        self.assertEqual(tensors["buffer_entries"].item(), 0)
        self.assertEqual(tensors["missing_keys"].item(), 0)
        self.assertEqual(tensors["unexpected_keys"].item(), 0)
        self.assertEqual(tensors["maximum_reload_difference"].item(), 0.0)

    def test_optimizer_state_is_distinct_and_populated_after_step(self) -> None:
        tensors = example.compute()
        self.assertEqual(tensors["training_step"].item(), 1)
        self.assertEqual(tensors["optimizer_step"].item(), 1)
        self.assertEqual(tensors["optimizer_parameter_states"].item(), 12)
        self.assertEqual(tensors["optimizer_slots_per_parameter"].item(), 3)
        self.assertGreater(tensors["embedding_update_norm"].item(), 0.0)


if __name__ == "__main__":
    unittest.main()

