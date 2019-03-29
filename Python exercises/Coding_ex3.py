my_variable = "hello"
print(my_variable[0]) # prints first letter in the my_variable string

for character in my_variable :
    print(character)

# ask user if he wants a number
user_wants_number = True
while user_wants_number ==True :
    print(10)

    user_input = input ("Should we print again Y/N? ")
    if user_input == "n" :
        user_wants_number = False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []

    for number in numbers:
        x = number % 2
        if x == 0 :
            evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice =="q" :
        return "Quit"
