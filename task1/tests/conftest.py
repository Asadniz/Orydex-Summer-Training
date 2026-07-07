"""Make the task1 solution modules importable from the tests folder."""

import pathlib
import sys

# task1/ is the parent of this tests/ directory.
TASK1_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK1_DIR))
