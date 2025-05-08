import webbrowser
import random 

dict = {
    "facebook": 'https://www.facebook.com/',
    "x": 'https://x.com',
    "twitter": 'https://x.com',
    "youtube": 'https://youtube.com'
}

input_user = random.choice(list(dict))

if input_user.lower() in dict:
    webbrowser.open(dict[input_user.lower()])
else:
    print("This website doesn't exist")
    
