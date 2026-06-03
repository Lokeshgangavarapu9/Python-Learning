# list example
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
my_list.append(6) # add 6 to the end of the list
print(my_list) # [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0) # add 0 to the beginning of the list
print(my_list) # [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3) # remove 3 from the list
print(my_list) # [0, 1, 2, 4, 5, 6]
my_list.pop() # remove the last element from the list
print(my_list) # [0, 1, 2, 4, 5]
my_list.pop(0) # remove the first element from the list
print(my_list) # [1, 2, 4, 5]
my_list[0] = 10 # change the first element of the list to 10
print(my_list) # [10, 2, 4, 5]
my_list.extend([120]) # add 120 to the end of the list
print(my_list) # [10, 2, 4, 5, 120]
my_list.insert(1,3)
print(my_list) # [10, 3, 2, 4, 5, 120]
print(my_list[0:2:3]) 

#string example
my_string = "hello world"
print(my_string) # hello world
my_string = my_string.upper() # convert the string to uppercase
print(my_string) # HELLO WORLD
my_string = my_string.lower() # convert the string to lowercase
print(my_string) # hello world

#srting in list
my_list = ["hello", "world"]
print(my_list) # ['hello', 'world']
my_list[0] = my_list[0].upper() # convert the first element of the list to uppercase
print(my_list) # ['HELLO', 'world']
my_list[1] = my_list[1].lower() # convert the second element of the list to lowercase
print(my_list) # ['HELLO', 'world']
print(len(my_list)) # 2