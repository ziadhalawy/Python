DB = [
    {"name": "ziad", "pass": "pass123"},
    {"name": "ahmed", "pass": "ahmemed"},
    {"name": "jes", "pass": "jessy"}
]




def dict_ex( user, password):

    for i in DB:
        
        if i["name"] == user:
            if i["pass"] == password:
                print("Login successful!")
                break
            else:
                print("Incorrect password!")
                break
        else:
            print("Username not found!")
            break
    

    
