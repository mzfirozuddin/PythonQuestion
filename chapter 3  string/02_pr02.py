"""write a prigram to fill in a letter template given below with name and date:

        letter=''' Dear <|NAME|>
                   You are selected!
                  <|DATE|>'''
           
"""

letter=''' Dear <|NAME|>
You are selected!
<|DATE|>'''

name=input("Enter your name:\n")
date=input("Enter date:\n")

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)


