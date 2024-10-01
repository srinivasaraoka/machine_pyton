from imp_python_files.pytest_1_program_write_class_tables_example import print_table
import os
#import pytest
'''
pytest, methods must start name with test_

Pytest it automatically fetch python program for pytest

pytest not required to call methods in program, pytest will call automatically


/Users/macairbook/Desktop/python_training/mymath/.venv/bin/pytest -v /Users/macairbook/Desktop/python_training/mymath/imp_python_files/program_test_pytest.py

'''


def test_output_file():
    obj2= print_table(4)
    obj2.print_table()  
    assert os.path.exists('output.txt')

def test_count_lines():
    f2= open('output.txt', 'r')
    count=0
    for lines in f2:
        count+=1
    assert count==10    