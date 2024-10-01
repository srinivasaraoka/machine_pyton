class print_table:
    def __init__(self, num):
        self.num= num

    def print_table(self): 
        f=open("output.txt", 'w')
        for var in range(1,11):
            
            print(f'{self.num} X {var} = {self.num*var}', file=f)
        

obj1=print_table(8)  
obj1.print_table()          
