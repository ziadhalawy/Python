def mario_pyr(num):

        for i in range(1, num + 1):
                spaces = ' ' * (num - i)
                printaple = (f"{num}" * i)
                print( spaces + printaple)

num = int(input("Please insert a num: "))
mario_pyr(num)
