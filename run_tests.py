import os
import sys
import subprocess


path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "environment", "PYTHONPATH")
)
sys.path.append(path)

path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "environment", "LUCIDITY_TEMPLATE_PATH"
    )
)
os.environ["LUCIDITY_TEMPLATE_PATH"] = path

subprocess.call(["pip", "install", "pytest"])
subprocess.call(["pip", "install", "lucidity"])

import pytest
pytest.main(
    [os.path.abspath(os.path.join(os.path.dirname(__file__), "tests"))]
)
