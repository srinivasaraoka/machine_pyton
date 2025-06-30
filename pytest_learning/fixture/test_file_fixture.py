import pytest
import os
# pytest.fixture is a decorator that is used to mark a function as a fixture. 
# Fixtures are used to provide a fixed baseline upon which tests can be run.
# pytest.fixture is used to share the object across multiple test cases.
# Fixtures are used to feed some data to the tests such as database connections,
#fixture are help to setup and teardown the test cases
#fixture will used code reusebility 
#pyython -m pytest .\test_file_fixture_scopr.py -v -s 
#pytest print will not not work, so we are using -s to print the output
"""

Feature         	What It Solves
Reusability	        Avoid copy-paste setup code
Clean test logic	Keeps test functions short and focused
Auto cleanup	    yield lets you tear down resources
Flexible scope    	Run once per test / module / session
Param injection		No need for manual setup calls


"""
@pytest.fixture
def test_file():
    print('\n creating file')
    f = open('test_file.txt', 'a+')
    return f
def test_write_ten_lines(test_file): #test_file is the fixture name which is used to call the fixture, 
    print('\n writing ten lines')
    num_lines_before= sum(1 for line in open('test_file.txt'))
    for i in range(10):
        test_file.write('X Y Z %d\n' % (i+1))
    test_file.flush()
    num_lines_after= sum(1 for line in open('test_file.txt'))
    print('\n number of lines before writing: ', num_lines_before)
    assert (num_lines_before+10) == num_lines_after
    test_file.close()  
    
def test_file_size_on_write(test_file):
    print('\n Writing one line')
    size_before = os.stat(test_file.name).st_size
    test_file.write('A B C 1\n')
    test_file.flush()
    size_after = os.stat(test_file.name).st_size
    assert (size_after-size_before) >= 0
    test_file.close()

        