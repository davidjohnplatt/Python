#!/usr/bin/env python
# The formula I used:
#M = L * ((I * ((1+I) ** n)) / ((1+I) ** n - 1))

# My code (probably not very eloquent but it worked)

# monthly payment
M = None
# loan_amount
L = None
# interest rate
I = None
# number of payments
n = None

L = 25000;
L = float(L)
print ('%s $%.2f' % ("Principal                  = ",L));

I = 4.9;
MI = float(I)/100/12
print ("Interest Rate              = " + str(I));

n = 60;
n = float(n)
print ("Number of Monthly Payments = " + str(n));

M = L * ((MI * ((1+MI) ** n)) / ((1+MI) ** n - 1))

#M = str(M)
print("\n")
print('%s $%.2f' % ("Monthly payment            = " , M));