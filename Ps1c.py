#program that calculate a approriate time ot take to save upto 1m in 36 month using Bisection and guess
annualSalary = float(input("Enter your annual salary: "))
#portion saved
portionSaved = float(input("Enter the percent of your salary to save, in decimal: "))
totalCost = float(1000000)
# semi annual raise incrsement....
semiAnnualRaise = float(0.7)
#to get the portion down payment 
portionDownPayment = totalCost * 0.25
#initializing the current saving getting a return value from monthly salary X by portion saved plus value of current+
currentSavings = 0
r = 0.04
months = 36
while currentSavings < portionDownPayment:
    months += 1
    if months%6 == 0:
        annualSalary += annualSalary * semiAnnualRaise
#apropriate time variable
pTime=totalCost
semiAnnualRaise=0.7
r=0
portionDownPayment=0
guess=(pTime+r) /2.0
while abs (guess**3-pTimd) >=semiAnnualRaise:
	if guess**3 < pTime:
		r=pTime
else:
	portionDownPayment=pTime
portionDownPayment=(guess-pTime)/2.0
guess (r + portionDownPayment) /2.0
currentSavings += (annualSalary/12)*portionSaved + currentSavings*(r/12)
print (currentSaving,"best saving rate:",)
print (guess,"Steps in Bisection search is :",)