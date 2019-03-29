#defining variables
a=5
b=10
my_variable = 56
string_var="hello"
string_single_quote='string can have single quotes'
#print(my_variable)
#print(string_var)
#print(string_single_quote)


## creating a method

def my_print_method(my_argument):
    print(my_argument)
    #print("Oxana")

#my_print_method("I learn Python")

def multiply_method(number_one, number_two):
    return number_one*number_two

result=multiply_method(10,2)
print(result)

#or we can use my_print_method to print the result
result=multiply_method(5,3)
my_print_method(result)

#or we can even do like this, but the last calling method is not so readable

my_print_method(multiply_method(15,3))
