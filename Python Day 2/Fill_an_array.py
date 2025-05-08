


def fill_arr(num_of_occ):
    list_inputs = []
        
    for i in range(num_of_occ):
        user_input = int(input(f"please insert the numbers to be added in the list num {i+1} =  "))
        list_inputs.append(user_input)

    print (sorted(list_inputs))
    print (sorted(list_inputs, reverse=1))

