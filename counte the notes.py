amount =int{input{"Please Enter Yokur Amount For Withdraw: "}}
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print{"notes of 100 taka" , note_1}
print{"notes of 50 taka" , note_2}
print{"notes of 10 taka" , note_3}
