givenPhrase = input("\nPlease input a phrase: ")

if givenPhrase == "" :
    print("\nPlease provide something!")
    exit(0)
else:
    phrase = givenPhrase

string = phrase.lower()

if string == string[::-1]:
    print("\nWow!, The phrase is a Palindrome!")
else:
    print("\nSorry, The given phrase is not a Palindrome.")