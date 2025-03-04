class Node:
    def __init__(self, data):
        self.data=data
        self.ref= None #self.head first node, self.head.ref next node

class LinkedList:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        if self.head==None:
            print("linked list empty")    
        else:
            n=self.head
            while n is not None:
                print(n.data, '---->',end=' ')
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head   
        self.head=new_node    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
        else:
            #n menas node(data+ref, n.data, n.ref)
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node  
    def add_after(self,data,x):
        n=self.head  
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("linked list empty")
        else:
            new_node=Node(data) 
            new_node.ref=n.ref
            n.ref=new_node# it will confuce fucus more (n is location of current node, n.ref is next node location)   
    def add_before(self,data,x):
        if self.head.data is None:
            print("linked list empty")
            return

        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node 
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x: 
               break
            n=n.ref
        if n.ref is None:
            print("data not found") 
        else:       
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node     
    def insert_empty(self,data):
        if self.head is None:
           new_node=Node(data)
           self.head=new_node 
        else:
            print("linked list is not empty")    
    def del_begin(self):
        if self.head is None:
            print("canot del")  
            return            
        else:
            self.head=self.head.ref
            return
    def del_end(self):
       
        if self.head is None:
            print("linked list empty")
            return
        n=self.head
        while n.ref.ref is not None:
            n=n.ref   
        n.ref=None #n.ref current node ref, n.ref.ref loction of after node
        return
    def del_node(self,x):
        if self.head is None:
            print("linked list is empty")
        if self.head.data==x:
            self.head=self.head.ref
        n=self.head 
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("delate data is not found")
        else:
            n.ref=n.ref.ref   
        return            
    
            
 
            
                   

                     
LL=LinkedList() 
LL.insert_empty(7)
LL.add_begin(10)
LL.add_begin(20)
#LL.insert_empty(20)
#LL.del_begin()
LL.add_before(8,10)

#LL.print_linkedlist()  
#LL.del_end()
#LL.add_before(9,20)
#LL.del_end()
#LL.add_after(150,100)
#LL.add_begin(20)
LL.print_linkedlist()      
LL.del_node(8)
LL.print_linkedlist()  
         