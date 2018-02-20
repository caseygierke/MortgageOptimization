# MortgagePaydown.py

# This code examines the mortgage structure and
# attempts to identify the optimum paydown 
# schedule by minimizing pay-in and interest 
# paid amounts while maximizing the value of
# dollars spent on paydown. 

# For compiling from Notepad++
# C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"

# -------------------------------------------
# IMPORTS
# -------------------------------------------

import matplotlib.pyplot as plt

git config --global core.editor “‘C:/Program Files/Notepad++/notepad++.exe’ -multiInst -notabbar -nosession -noPlugin”
# -------------------------------------------
# INPUTS
# -------------------------------------------

P = 280000 			# Initial principle value
r = 6.0 			# Interest rate
N = 360 			# Number of months mortgaged
CF = 2421.26
extra = CF*0.5

# Initialize array for each month
Narray = range(N+1)

# Open variables for tracking dollars
Parray = [P] 		# Principle left during amortization
PrinPaidWO = [0]	# Principle paid during amortization
IntPaidWO = [0]		# Interest paid during amortization
PWarray = [P] 		# Principle left during amortization with paydown
PrinPaidW = [0]	# Principle paid during amortization
IntPaidW = [0]		# Interest paid during amortization

# -------------------------------------------
# CALCULATIONS
# -------------------------------------------

# Calculate the fixed monthly payment
MP = P*(r/100/12*(1+r/100/12)**360)/((1+r/100/12)**360-1)

# Open loop to make calculations
for i in range(1,N+1):
	
	# Calculate the baseline mortgage with no pay down
	Parray.append((1+r/100/12)**Narray[i]*P - (((1+r/100/12)**Narray[i]-1)/(r/100/12))*MP)
	PrinPaidWO.append(Parray[i-1] - Parray[i])
	IntPaidWO.append(Parray[i-1]*r/100/12)
	
	# Calculate the changes with extra paid
	PWarray.append((1+r/100/12)*PWarray[i-1] - (((1+r/100/12)-1)/(r/100/12))*MP - extra)
	# We have to check that the mortgage still has a balance
	if PWarray[i] > 0:
		PrinPaidW.append(PWarray[i-1] - PWarray[i])
		IntPaidW.append(PWarray[i-1]*r/100/12)
	else:
		PrinPaidW.append(0)
		IntPaidW.append(0)
	
# -------------------------------------------
# OUTPUTS
# -------------------------------------------

plt.plot(Narray, Parray, '-k')
plt.plot(Narray, PWarray, '-b')

plt.ylim(0,P*1.1)
labels = ['Prin- Standard', 'Prin With Paydown',]
plt.legend(labels)

plt.show()