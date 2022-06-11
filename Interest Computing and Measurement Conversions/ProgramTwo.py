#Prompting User
miles = eval(input('How many miles? '))
yards = eval(input('How many yards? '))
feet = eval(input('How many feet? '))
inches = eval(input('How many inches? '))

#Converting to find total inches
mi = miles * 5280 * 12
yd = yards * 3 * 12
ft = feet * 12
totalInches = mi + yd + ft + inches

#Converting to metric
km = totalInches // 39370.1
km = int(km)
inchesLeft1 = totalInches % 39370.1
m = inchesLeft1 // 39.37
m = int(m)
inchesLeft2 = inchesLeft1 % 39.37
cm = inchesLeft2 / 0.393701
cm = round(cm, 1)

#Display
print('Metric Length:','\n',km,'kilometers','\n',
        m, 'meters','\n',cm,'centimeters')