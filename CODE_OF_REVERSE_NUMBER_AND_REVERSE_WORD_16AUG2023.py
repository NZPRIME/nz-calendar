number=int(input("Enter Any Number: "))
b=str(number)
l=len(b)
print("Digit Count Of Number Which You Input: ",l)
variable=""
for i in range (l):
    remainder=number%10
    print("Remainder From Number Divided: ",remainder)
    number=number//10
    print("Remaining Number Excluding Remainder: ",number)
    remainder=str(remainder)
    variable=variable+remainder
print("Reversed Number Of Input Number: ",variable)
print("=============================")
word=input("Enter Any word: ")
l=len(word)
print("Total Character Count:",l)
print("Reverse Of input Word: ",word[l: :-1])


