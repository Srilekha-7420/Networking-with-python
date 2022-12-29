import pytest
@pytest.mark.parametrize("a,b,c",[(1,2,3),(7,8,15)])
def test_functionAdd(a,b,c):
    assert a+b==c
@pytest.mark