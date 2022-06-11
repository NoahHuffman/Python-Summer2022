#Prompting User
a = eval(input('What is the amount of the loan? '))
r = eval(input('What is the interest rate? '))
n = eval(input('How many years will you be making the payments? '))

#Computing Monthly Payment
i = r/1200
monthly = (i / (1-(1+i)**(-12*n))) * a
answer = round(monthly,2)

#Display
answer = str(answer)
str1 = 'The monthly payment will be $'+answer
print(str1)