a= 100
b= [1,2,3,4]
s= list(map( lambda x : x*x, b))
print(s)
y= list(filter(lambda x:x%2==0, b))
print(y)


def many(func):
    def inner(z):
        print('hi')
        print(z)
        func(7)
        return
    return inner

@many
def print_func(x):
    print('srinivas good', x)
    return 
print_func(5)    
