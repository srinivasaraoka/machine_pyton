class A:
    a=10
    def __init__(self,name):
        self.name= name
    def reversed(self, num):
        rev=0
        num= int(num)
        while num >0:
            digit= num%10
            rev= rev*10+digit
            num= num//10
        return rev 
        
    def prime(self, number):
        flag=None
        num1= self.reversed(number)
        for i in range(1, num1//2+1):
            if num1%i==0:
                flag= False
            else:
                flag= True
        print('given number is ', flag)    
    def excpt(self,a,b):
        try:
            dev=a/b
        except Exception as e:
            print('we are getiing exception please enter b value none zero', e)
            
    def mul(self, *args):
        total=0 
        for x in args:
            total =total+x
        print(total)
    
            
            

obj1= A('srini')   
z=obj1.reversed(209)
y= obj1.prime('17')
obj1.excpt(10,1)
print(y)
obj1.mul(1,2)
obj1.mul(1,2,3)
1, what are oprators in python