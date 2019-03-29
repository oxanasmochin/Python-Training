list_of_grades = [10, 4, 7, 6, 5]   #List
tupel_of_grades = (10, 4, 7, 6, 5)  #tupels are immutabel
set_of_grades = {8, 9, 3, 5, 8}  # set contains elements that are unique and unordered

tupel_of_grades = tupel_of_grades+ (100,) #adding two tupels together
#print(tupel_of_grades)

#print(list_of_grades[0])    #prints the first element that have position 0
list_of_grades[0]=34    # assign a new element to the list_of_grades, but this
                        #cannot be done in a tupel because tupel is immutabel


#print(len(list_of_grades))       # len is a method calculating length of a list
#print(sum(list_of_grades)/len(list_of_grades)) #calculates avarage of grades

list_of_grades.append(8)
#print(list_of_grades)

#print(set_of_grades)

# Advanced set of operations
my_lottery_numbers={1, 2, 3, 4, 5}
winning_lottery_numbers={1, 3, 5, 7, 9}
print(my_lottery_numbers.intersection(winning_lottery_numbers)) #prints what common numbers exist in both sets
print(my_lottery_numbers.union(winning_lottery_numbers)) #unites two sets
print(my_lottery_numbers.difference(winning_lottery_numbers)) # shows what differentiates two sets
