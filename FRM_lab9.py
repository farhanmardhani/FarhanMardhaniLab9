#Grant Burling
#Farhan Mardhani


def menu ():
    print ('''
Menu
-------------
1. Encode
2. Decode
3. Quit
    ''')

def encoder (number):
    list = []
    for i in range(0, len(number)):
        list.append(int(number[i]))
    for i in range(0, len(list)):
        list[i] = (list[i] + 3) % 10
        list[i] = str(list [i])
    return "".join(list)

def decoder(number):
    list = []
    for i in range(0, len(encoder(number))):
        list.append(int(number[i]))
    for i in range(0, len(list)):
        list[i] = (list[i] - 3)
        if list[i] < 0:
            list[i] = list[i] + 10
    for i in range(0, len(list)):
        list[i] = str(list[i])
    return "".join(list)

def main ():
    option = 0
    while option != 3:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            number = str(input("Please enter your password to encode: "))
            print (encoder(number))
            print ("Your password has been encoded and stored!")
            print ("")
        if option ==2:
            en = (encoder(number))
            de = (decoder(en))
            print (f"The encoded password is {en}, and the orginal password is {de}")
        if option == 3:
            break

if __name__ == "__main__":
    main()