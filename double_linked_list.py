class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DL:
    def __init__(self):
        self.head= None

    def print_dl(self):
        if self.head==None:
            print("Double linked list empty")
            
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->", end=' ')
                n=n.nref
          
    def print_bw_dl(self):
        print()
        if self.head==None:
            print("Double linked list empty")    
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print("<--",n.data,end=" ")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head= new_node
        else:
            print("linked list is empty1")    
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            
            self.head= new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:    
            n=self.head
            while n.nref is not None:
                n=n.nref 
            n.nref=new_node  
            new_node.pref=n 
    def add_after(self,data,x):
        if self.head is None:
            print("linked list empty we cannot add") 
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.nref
        if n is None:
            print("x not found")
        else:
            new_node=Node(data)
            new_node.nref=n.nref
            new_node.pref=n
            if n.nref is not None:
                n.nref.pref=new_node #n is current node, n.nref is nextnode, n.nref.oref nexnode pref
            n.nref=new_node  
    def add_before(self,data,x):
        if self.head is None:
            print("linked list empty we cannot add") 
        n=self.head
        while n is not None:
            if n.data==x:
                break  
            n=n.nref
        if n is None:
            print("x not found")
        else:
            new_node=Node(data)
            
            new_node.nref=n
            new_node.pref=n.pref
            if n.pref is not None:
                n.pref.nref=new_node #n is current node, n.pref perviusnode, n.pref.nref is perviues node nref
            else:
                self.head=new_node           
            n.pref=new_node    

    def del_begin(self):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None    

    def del_end(self):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            self.head=None
        else:    
            n=self.head
            while n.nref is None:
                break
            n.nref=None

    def del_node(self,x):
        if self.head is None:
            print("double linked list is empty") 
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("given node not found")    
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return

        n=self.head
        while n.nref is not None:
            if n.data==x:
                break
            n=n.nref
        if n.nref is not None:
            n.pref.nref=n.nref 
            n.nref.pref=n.pref 
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("x not found")        

             
       




            





        
dl=DL()
#dl.print_dl()
dl.insert_empty(20)
#dl.print_dl()
dl.add_begin(10)
dl.add_end(30)
dl.add_after(40,30)
dl.add_before(5,10)
dl.del_node(10)
dl.del_begin()
dl.del_end()
dl.print_dl()






