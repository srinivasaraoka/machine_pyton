'''  Auther: Srinivas '''
import pytest

def divide(devidend, devisor):
    return devidend/devisor

def test_divide_pass():
    assert divide(10,2) == 5
    
#  def test_divide_error_zero():
#     assert divide(10,0) == 5   
    
def test_divide_error_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
    #assert divide(10,0) == 5
    
def test_divide_error_type():
    assert divide(10,'a') == 5    