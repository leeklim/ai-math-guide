from __future__ import annotations

import unittest

from scripts.run_n05_examples import load_examples
from scripts.site import load_n05_example_registry


class ExampleRegistryTest(unittest.TestCase):
    def test_runner_and_site_use_the_same_examples(self) -> None:
        runner_examples = load_examples()
        site_registry = load_n05_example_registry()
        self.assertEqual(len(runner_examples), 10)
        self.assertEqual(len(site_registry), 10)
        self.assertEqual(
            {example_id for example_id, _ in runner_examples},
            {str(entry["example_id"]) for entry in site_registry.values()},
        )
        self.assertEqual(list(site_registry), [f"N05-{number:02d}" for number in range(1, 11)])


if __name__ == "__main__":
    unittest.main()
