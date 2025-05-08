
def emailValidation(email):
   # email = "test@gmail.com" #input("Please Enter a valid email: ")
    splitted_string = email.split('@')
   
    while ( 
           email.__contains__('@') and 
           splitted_string[0] != 0 and 
           splitted_string[0][-1].isalnum() or 
           splitted_string[0][-1].isalpha() and 
           splitted_string[1].__contains__('.') and 
           splitted_string[1][0] != '.' and 
           splitted_string[1][-1] != '.'
           ):
        print("valid")
        break
    else:
        print("not valid")
        email_input = input("Please ReEnter a valid email: ")





#email = "test@gmail.com" #input("Please Enter a valid email: ")
#splitted_string = email.split('@')
#print( )