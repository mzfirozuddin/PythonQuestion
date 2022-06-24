sub1=int(input("Enter first sub marks: "))
sub2=int(input("Enter second sub marks: "))
sub3=int(input("Enter third sub marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail!")
elif((sub1+sub2+sub3)/3<40):
    print("you are fail due to total percentage less than 40")
else:
    print("Congratulation! you passed the exam.")