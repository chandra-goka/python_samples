#define decorator @ sign
def sum_and_diff(func):
    def wrapper(num1,num2):
        print("difference is :" + str(num1-num2))
        return func(num1,num2)
    return wrapper

#define the function
@sum_and_diff
def add(num1,num2):
    print ("Sum is :" + str(num1+num2))

#Execute
add(5,10)

##########################################

#define decorator to new variable
def sum_and_diff(func):
    def wrapper(num1,num2):
        print("difference is :" + str(num1-num2))
        return func(num1,num2)
    return wrapper

#define the function
def add(num1,num2):
    print ("Sum is :" + str(num1+num2))

#Execute
add_diff=sum_and_diff(add)
add_diff(5,10)
print("_______________")
add(5,10)

##########################################

#define decorator class @sign
class sum_and_diff_by_class(object):
    def __init__(self,func):
        self.func=func
    def __call__(self,num1,num2):
        print("difference is :"+ str(num1-num2))
        return self.func(num1,num2)

if __name__ == '__main__':
    #define initial function
    @sum_and_diff_by_class
    def add(num1,num2):
        print ("Sum is :" + str(num1+num2))
    #Execute
    add(5,10)

##########################################

#define decorator class new variable
class sum_and_diff_by_class(object):
    def __init__(self,func):
        self.func=func
    def __call__(self,num1,num2):
        print("difference is :"+ str(num1-num2))
        return self.func(num1,num2)

if __name__ == '__main__':
    #define initial function
    def add(num1,num2):
        print ("Sum is :" + str(num1+num2))

    #Execution
    new_fun=sum_and_diff_by_class(add)
    new_fun(5,10)
    print("_____________")
    add(5,10)
