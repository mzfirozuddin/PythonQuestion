"""spam message detector"""

text=input("Enter the text: ")

if("make lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")