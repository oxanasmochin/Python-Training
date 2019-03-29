def who_do_you_know ():
    # Ask a user for a list of people they know
    # split a string into a list
    # return that list
    people = input("Enter names of people you know separated by commas: ") #Oxana,Asti,Stefan
    people = people.replace(" ","") #cleans white spaces
    people_list = people.split(",")  # ["Oxana" , "Asti", "Stefan"]

    return people_list

def ask_user ():
    #Ask a user to enter a name
    # See if the name exists in the people_list
    person = input("Enter a name of somebody you know: ")
    if person in who_do_you_know() :
        print("You know {}! " .format(person))
    else :
        print("You do not know anyone!")

ask_user()
