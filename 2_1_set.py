
set2= {1,2,3,4}

# Number of test cases
set1= set()
t = int(input())
# Process each test case
for _ in range(t):
    # Number of elements in set A (not needed for logic)
    n = int(input()) 
    # Elements of set A
    A = set(map(int, input().split()))
    
    # Number of elements in set B (not needed for logic)
    m = int(input())
    
    # Elements of set B
    B = set(map(int, input().split()))
    
    # Check if A is a subset of B
    if A.issubset(B):
        print(True)
    else:
        print(False)
