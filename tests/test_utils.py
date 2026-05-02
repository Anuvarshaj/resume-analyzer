import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import clean_text

def test_clean_text():
    assert clean_text("  HELLO ") == "hello"