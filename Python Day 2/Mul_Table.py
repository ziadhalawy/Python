def mul_table(user_input):
    ll = []

    for i in range(user_input):
        row = []  
        for j in range(i + 1):  
            row.append((i + 1) * (j + 1))  
        ll.append(row)  

    print(ll)
    row.clear()


