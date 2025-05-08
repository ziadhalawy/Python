'''
user_input = input("Please Enter your nam (alphabeticals only): ")
for i in range(len(user_input)):
    if 'a' <= user_input[i] >= 'Z':
        print("Validated Succefully")
        break
    else:
       print( "please insert a alphabeticals only")
       break

'''
email_input = "z.halawy@gmail.com" #input("Please Enter a valid email: ")

splited_string = email_input.split('@')

splited_string[0][-1] != '.'

"""
email_input = "z.halawy@gmail.com" #input("Please Enter a valid email: ")

splited_string = email_input.split('@')

plited_string[0][-1]

while email_input.__contains__('@') and splited_string[1].__contains__('.') and splited_string[1][0] != '.' and splited_string[1][-1] != '.':
    print("valid")
    break
else:
    print("not valid")
    """


