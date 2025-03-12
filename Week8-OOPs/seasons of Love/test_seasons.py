from seasons import age
from datetime import date

def test_main():
    assert age("1999", "01", "01", date.fromisoformat("2000-01-01")) == "Five hundred twenty-five thousand, six hundred minutes"
    assert age("2023", "10", "11", date.fromisoformat("2023-10-12")) == "One thousand, four hundred forty minutes"
    assert age("1993", "10", "12", date.fromisoformat("2023-10-12")) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    assert age("2001", "01", "01", date.fromisoformat("2003-01-01")) == "One million, fifty-one thousand, two hundred minutes"