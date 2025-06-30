import pytest
import os

@pytest.fixture
def write_file():
    print('\ncreating the file')
    f= open('append_file.txt', 'w+')
    for i in range(10):
        f.write('\nX yZ %d' % (i+1))1
    f.flush()
    yield f
    print('\n closing the file')
    f.close()
    
@pytest.fixture
def readonly_file():
    print('\n Creating file')
    f= open('readonly_file.txt', 'w+')
    for i in range(10):
        f.write('\nX Y Z %d' % (i+1))
    f.close()
    f= open('readonly_file.txt','r') 
    yield f     
    print("\n closing the file")  
    f.close()   
        