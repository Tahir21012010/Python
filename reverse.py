# Input a word or Sentence
string = input ("lease enter your own Srring : ")
string2 = ('')
# loop for printing in reverse
for i in string:
    string2 = i + string2
print("\nThe Original Sring = ", string)
print("The reverse String = ", string2)