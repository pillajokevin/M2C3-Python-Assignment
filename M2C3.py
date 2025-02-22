# M2C3-Python-Assignment 

# Exercise 1 

my_string = "Hello i'm Kevin" #Esto es una cadena 

the_number = 28 # Esto es un numero 

my_list = [1 ,2 ,3 ,4, 5 ]

the_boolean = True

# print(my_string)
# print(the_number)
# print(my_list)
# print(the_boolean)


# Exercise 2 

first_three_letters = my_string[:3] # Aqui lo estamos guardando en una variable 
# print(first_three_letters)


# Exercise 3 

first_element = my_list[0] # aqui estamos tomando el primer elemento de mi lista 
# print(first_element)

# Exercise 4 

new_number = 10 
sum_result = the_number + new_number # Sumandole 10 al numero original
# print(sum_result)

# Exercise 5 

last_element = my_list[-1] # Hemos usado el negative index 
# print(last_element)


# Exercise 6 

names = "Harry,alex,susie,jared,gail,conner"

list_of_tags = names.split(",") #Estamos transformando la cadena en una lista 

# print(list_of_tags)




# Exercise 7 

space_index = my_string.find(' ') # Encontramos el primer espacio 

the_first_word =my_string[:space_index]  #  Obtenemos la primera palabra

# print(the_first_word) 

transform_letters = the_first_word.upper()# Obtenemos la primera palabra  en Mayusculas

# print(transform_letters)

upper_word = transform_letters + my_string[space_index:] # Obtenemos solo la primera palabra en Mayuscula

# print(upper_word)


# Exercise 8

# En este metodo he usado f-string que es mas sencillo y eficiente 
message = f"{my_string} y tengo {the_number} anos de edad ."

# print(message)


#Exercise 9 


# print("Hello world") 