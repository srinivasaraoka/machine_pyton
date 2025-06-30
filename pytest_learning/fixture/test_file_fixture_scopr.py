import pytest
import os

@pytest.fixture(scope= 'module')
def test_file():
    print('\n creating file')
    f = open('test_file.txt', 'a+')
    yield f
    print('\n closing the file')
    f.close()
    
def test_write_ten_lines(test_file):
    print('\n writing ten lines')
    num_lines_before= sum(1 for line in open('test_file.txt'))
    for i in range(10):
        test_file.write('X Y Z %d\n' % (i+1))
    test_file.flush()
    num_lines_after= sum(1 for line in open('test_file.txt'))
    print('\n number of lines before writing: ', num_lines_before)
    assert (num_lines_before+10) == num_lines_after # once the test case is completed, the file will be closed automatically, it will go to the yield statement and close the file
    
    
def test_file_size_on_write(test_file):
    print('\n Writing one line')
    size_before = os.stat(test_file.name).st_size
    test_file.write('A B C 1\n')
    test_file.flush()
    size_after = os.stat(test_file.name).st_size
    assert (size_after-size_before) >= 0
       