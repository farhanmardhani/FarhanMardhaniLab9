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
    for i in range (0,len(number)):
        list.append(int(number[i]))
    for i in range (0,len(list)):
        list [i] = (list[i] + 3)%10
    list [i] = str(list [i])
    return "".join(list)

def decoder ():
    pass

def main ():
    option = 0
    while option != 3:
        menu()
        option = int(input("Please enter an option: "))
        number = int(input("Please enter your password to encode: "))
        if option ==1:
            print (encoder(number))
            print ("Your password has been encoded and stored!")
            print ("")
        if option ==2:
            encode = encoder(number)
            decode = decoder(number)
            print (f"The endoded password is {encode}, and the orginal password is {decode}")
        if option == 3:
            break

if __name__ == "__main__":
    main()