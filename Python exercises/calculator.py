numberOne = input("Enter first number: ")
numberTwo = input("Enter second number: ")
menu = "Please select en option from menu\n (1)- Addition\n (2)- Substraction\n (3)-Multiplication\n (4)- Division\n "
choice = input ("Your choice: ")

if choice == "1" :
    operation=int(numberOne)+int(numberTwo)
    print(str(operation))
elif choice == "2" :
    operation=int(numberOne)-int(numberTwo)
    print(str(operation))
elif choice == "3" :
    operation=int(numberOne)*int(numberTwo)
    print(str(operation))
elif choice == "4" :
    if numberTwo == "0" :
        print("Error division by 0")
        break;
    else:
    operation=int(numberOne)/int(numberTwo)
    print(str(operation))
