'''  Auther: Srinivas '''
#python -m pytest C:\Users\kagsrini\machine_pyton\test_sample.py
# check any defination start with test_ in the file

def rectangle(length, width):
    return 2*length * width
def test_perimeter():
    assert rectangle(5, 10) == 100
def perimeter_test():
    assert rectangle(5, 10) == 100    