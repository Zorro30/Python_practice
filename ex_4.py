def LetterChanges(str): 

    
    newstring = ""
    for char in str:
        
        if char.isalpha():
            
            if char.lower() == 'z':
                char = 'a'
                
            else:
                char = chr(ord(char)+1)
            
        if char in 'aeiou':
            char = char.upper()
        
        newstring = newstring + char
            
    return newstring
    
print(LetterChanges(input("Input your word or phrase:")))