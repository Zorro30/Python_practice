import include

def main():

    print ("Do you love cricket?")
    print ("You'll have to select between T20 or Test cricket")

    option = int(input("Enter your choice '1' for T20 and '2' for Test:"\
                        "\n>"))

    if option == 1:
        include.T20()
    elif option == 2:
        include.Test()
    else :
        print ("You should try some other sport.")

main()
