""" The program:
Your program must output the facial composite of a wanted criminal from the description of a witness, given to you in the form of ascii characters.

The description consists of:
1 character for the hair.
1 character for the sides of the face.
1 character for the eyes.
1 character for the nose.
1 character for the mouth.
A string of 1,3 or 5 characters for the chin.
Each item separated by a space.

Do not include a trailing whitespace after the chin.

INPUT:
6 strings hair, cheek, eye, nose, mouth, chin.

OUTPUT:
The facial composite on 5 lines and 5 columns. The chin must be centered.

EXAMPLE:
Input
! | o V - \_/
Output
!!!!!
|o o|
| V |
| - |
 \_/ 
"""

hair, cheek, eye, nose, mouth, chin = input().split()
print(hair*5)
print(cheek + eye + ' ' + eye + cheek)
print(cheek + ' ' + nose + ' ' + cheek)
print(cheek + ' ' + mouth + ' ' + cheek)
if len(chin) ==1:
    print('  '+ chin)
elif len(chin) == 3:
    print(' '+ chin)
else:
    print(chin)
