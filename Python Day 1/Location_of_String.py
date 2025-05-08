
def detect_location(char):
    detected = []
    for j in range(len(char)):
        if char[j] == "i":
            detected.append("The location of 'i' shows up in index "+ " " + f"{j+1} ")
        else:
            
            return "No 'i's here"

    return detected

            