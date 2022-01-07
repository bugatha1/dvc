import pytest

class NotInRange(Exception):
    def __init__(self, message="value is not in the range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange

def test_assertmethod():
    a = 2
    b = 2
    assert a == b            