queue=[]
def enque():
    ele=input("enter input")
    queue.append(ele)
    print(queue)
def deque():
    if not queue:
        print("queue empty")    
    else:
        e=queue.pop(0)
        print(e)






while True:
    x= int(input("enter input:1,enque2,deque3,print4,display"))
    if x==1:
        enque()
    elif x==2:
        deque()
    else:
        break            


