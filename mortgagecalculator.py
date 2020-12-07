import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

sales_price = float(input('Please enter the cost of the house in US$: '))
down_payment = float(input('Please enter the amount of down payment as a porcentage of Sales Price. eg 10 for a 10%: '))
loan_amount = sales_price*(1-down_payment/100)
mortgage_time = float(input('Please enter the amount of time of you mortgage loan: eg 10 for 10 years: '))
loan_term = int(12*mortgage_time)
interest_rate = float(input('Please enter loan interest rate: eg 2 for 2%: '))
R = 1 + (interest_rate)/(12*100)

X = loan_amount *(R**loan_term)* (1-R)/ (1-R**loan_term)

monthly_interestrate = []
monthly_balance = []

for i in range(1,loan_term +1):
    Interest = loan_amount*(R-1)
    loan_amount = loan_amount - (X-Interest)
    monthly_interestrate = np.append(monthly_interestrate,Interest)
    monthly_balance = np.append(monthly_balance, loan_amount)


print('The home sales price is: = '+ str('$') + str(sales_price))
print('The down payment as a percentage of the sales price is: = ' + str(down_payment) + str(' %'))
print('The Loan Amount is: = ' + str(sales_price*(1-down_payment/100)) + str(' $'))
print('The interest rate on annual percentage basis is: = ' + str(interest_rate) + str(' %'))
print('The duration of this loan in months: ' + str(loan_term) + str('months'))
print('Monthly payment for this mortgage(P & I) is: = ' + str('$') + str(np.round(X,2)) )
print('Total interest paid over life cycle of the loan is: = ' + str('$') + str(np.round(np.sum(monthly_interestrate),2)))


#produce visualization of monthly loan balance and interest

plt.plot(range,(loan_term+1), monthly_interestrate, 'r',lw=2)
plt.xlabel('month')
plt.ylabel('monthly interest ($)')
plt.show()

#plt.plot(range(1,(loan_term+1), monthly_balance, 'b',lw=2)
#plt.xlabel('month')
#plt.ylabel('monthly loan balance ($) ')
#plt.show()