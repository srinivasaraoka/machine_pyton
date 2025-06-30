'''
Abstraction: representing essential features and hiding unnecessary details to 
simplify the complexity.(sunil nareina bowling)
Abstraction is about simplifying the interface, hiding complex details, and 
allowing the user to interact with the object without knowing the internal 
mechanics. It is implemented using abstract classes or methods.

'''

class Student:
    def __init__(self, name, rollnumber, age):
        self.name=name
        self._rollnumber=rollnumber
        self.__age=age
    def __displayprivatedata(self):
        print("hi how are u")    
    def display(self):
        print(f"{self.name} is {self.__age}") 
        self.__displayprivatedata()
class Branch(Student):
    #pass # it means all parent init methods instilize here
    def show(self):
        print(f"{self.name} is {self._rollnumber}") 
        #print(self.__age) # AttributeError:'Branch' object has no attribute '_Branch__age'

s1= Student("srinivas","123",28) 
s1.display() 
s2=Branch("hari", "321", 29)
s2.show()
s1.__displayprivatedata() #AttributeError:'Student' object has no attribute '__displayprivatedata'

