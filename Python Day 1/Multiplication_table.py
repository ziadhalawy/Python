def mul_table(user_input):
    num = int(user_input)

    for i in range(num):
        for j in range(num):
            if j == i:
                print(f"{i+1} * {j+1} = {(i+1)* (j+1)}")
                break
            else:
                    print(f"{i+1} * {j+1} = {(i+1)* (j+1)}")

