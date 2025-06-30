#python -m pytest -v #-v means to show the output of the test cases and fixtures. v means verbose
#python -m pytest -v -k test_type 
#python -m pytest -v -k "add" #it will run all the test cases which has "add" in the name
#python -m pytest -v -k "add or string" #it will run all the test cases which has "add" or "string" in the name
#python -m pytest -v -x
#python -m pytest -v -x --maxfail=2
#python -m pytest -v -x --maxfail=2 --tb= no #imp

# PS C:\Users\kagsrini\machine_pyton\pytest_learning> python -m pytest -v -x --maxfail=2 --tb=yes
# ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
# __main__.py: error: argument --tb: invalid choice: 'yes' (choose from 'auto', 'long', 'short', 'no', 'line', 'native')

# python -m pytest .\test_multiple_simple.py -v -m number #it will run all the test cases which has number in the marker
#python -m pytest -v -rsf #-rsf means to disable all the output capture and show the print statements in the console.
#python -m pytest -v -rsx #-rsx means to disable all the output capture and show the print statements in the console and stop the execution on first failure.
#python -m pytest -q  #quiet mode means only show the output of the test cases and not the fixtures.
#python -m pytest -v -q  #quiet mode means only show the output of the test cases and not the fixtures.
#python -m pytest --pdb #to start the debugger on the first failure.
#python -m pytest --maxfail=2 #to stop the execution on the 2nd failure.
 
import pytest

@pytest.mark.number
def test_type():
    assert type(1+2) is int

@pytest.mark.number
def test_add_int():
    assert 1+2 == 4
 
@pytest.mark.string    
def test_string():
    assert 'a' in 'cat'    
    
@pytest.mark.string 
@pytest.mark.skip(reason="do not run this test temprerrly ")
def test_add_string():
    assert ('sun' + 'day') == 'sunday'        