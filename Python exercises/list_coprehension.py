my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] #range(5) is a list [0, 1, 2, 3, 4]

multiply_list = [x*3 for x in range(5)] # result will be [0, 3, 6, 9, 12]
print(multiply_list)

even_list = [n for n in range(10) if n % 2 ==0] #result [0, 2, 4, 6, 8]
print(even_list)

people_list =["Asti", " Stefan", "andreas", "   Oxana"]
print(people_list)
edited_people_list = [person.strip().lower() for person in people_list] #result ['asti','stefan','andreas','oxana']
print(edited_people_list)
