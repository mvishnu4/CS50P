from working import convert
import pytest

def test_convert():
    assert convert("12:00 AM to 12:00 PM") == "12:00 to 00:00"
    assert convert("12 PM to 8:30 AM") == "00:00 to 08:30"