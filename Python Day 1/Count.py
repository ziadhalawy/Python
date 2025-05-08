
def vowel_count( input_num):
    vowelList = ["a","e","i","o","u"]
    counter = 0
    for i in range(len(input_num)):
        for j in range(len(vowelList)):
            if(input_num[i].lower() == vowelList[j]):
                counter+=1
                break
    return counter
            
    

