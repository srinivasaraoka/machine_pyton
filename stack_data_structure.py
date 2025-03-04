stack =[]
#first in last out, stack is bucket 
def push():
    x= input('enter element')
    stack.append(x)
    print(stack)

def pop():
    if not stack:
        print('stack empty')
    else:    
        stack.pop()
        print(stack)    
while True:
    choice=input("enter1,2,3")  
    if choice=='1':
        push()
    elif choice=='2':
        pop()
    else:
        break              