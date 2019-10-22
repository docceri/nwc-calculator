# Calculate Net Working Capital for next 2 months, variable percentages are coming externally
#
# 1 Start values
# 2 Variable percentages
# 3 Calculates NWC for next month
# Variables and signs:
#   nwc = net working capital (+/-) = inv + ar - ap
#   inv = inventory (+)
#   ar = accounts receivable (+)
#   ap = accounts payable (-)

# create variables
# nwc_fcst = 0

# inv = 0
# ar = 0
# ap = 0

# inv_var = 0
# ap_var = 0
# ar_var = 0

# 1 ask user to set the starting values
inv_start = input ("Enter the current value of the inventory (in absolute value): ")
inv_value = int(inv_start)

ar_start = input ("Enter the current value of the accounts receivable (in absolute value): ")
ar_value = int(ar_start)

ap_start = input ("Enter the current value of the accounts payable (in absolute value): ")
ap_value = int(ap_start)

nwc_start = inv_start + ar_start - ap_start

print ("Your current inventory is: " + str(inv_value))
print ("Your current accounts receivable is: " + str(ar_value))
print ("Your current accounts payable is: " + str(ap_value))
print ("Your current net working capital is: " + str(nwc_start))

# 2 enter the percentage changes for first and second month for every variable
inv_variable = input ("Enter the inventory growth percentage without % sign (e.g. -1 or 4): ")
inv_var = int(inv_variable)

ar_variable = input ("Enter the accounts receivable growth percentage without % sign (e.g. -1 or 4): ")
ar_var = int(ar_variable)

ap_variable= input ("Enter the accounts payable growth percentage without % sign (e.g. -1 or 4): ")
ap_var = int(ap_variable)

# 3 calculate and print the nwc and show the percentage change of nwc per month
inv_fcst = (inv_value * (1+(inv_var/100)))
ar_fcst = (ar_value * (1+(ar_var/100)))
ap_fcst = (ap_value * (1 + (ap_var / 100)))

nwc_fcst = inv_fcst + ar_fcst - ap_fcst

inv_growth = ((inv_fcst - inv_value) / inv_value) * 100
ar_growth = ((ar_fcst - ar_value) / ar_value) * 100
ap_growth = ((ap_fcst - ap_value) / ap_value) * 100

print("Growth percentages for inventory " + str(inv_growth) + "% , accounts receivable " + str(ar_growth) + "% and accounts payable " +  str(ap_growth) + "%")
print("Your next month calculated net working capital will be: " + str(nwc_fcst))
if nwc_fcst < 0:
    print("Good luck with that!")
if 0 < nwc_fcst < 100:
    print("Getting there, keep on going!")
if nwc_fcst > 100:
    print("Great job!")
