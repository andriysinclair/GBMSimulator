from pathlib import Path

# Inside GBMSimulator/__init__.py
from .GBMSimulator import GBMSimulator
'''Ensures that import GBMSimulator works'''

# Absolute path to the modules folder
modules_path = Path(__file__).parent.parent /  "GBMSimulator"
