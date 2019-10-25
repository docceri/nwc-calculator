# Calculate Net Working Capital for next month
# Growth percentages are given externally
#
# 1 Define function
# 2 Enter NWC values and calculate NWC
# 3 Enter growth percentages, calculate new NWC and show the growth percentages
# 4 Give verbal feedback
#
# Variables and signs:
#   nwc = net working capital (+/-) (= inv + ar - ap)
#   inv = inventory (+)
#   ar = accounts receivable (+)
#   ap = accounts payable (-)

# 1 defining nwc_calc function
# this function is also used to calculate NWC after setting the growth percentages
# if the growth percentage is not defined, then it will be 1 -> given input value will not change
# e.g. AR 2 * 1 (when no growth) = 2


def nwc_calc(inv, ar, ap, inv_growth=1.0, ar_growth=1.0, ap_growth=1.0):
    """Function is calculating NWC and new NWC"""
    nwc = (inv * (1 + (inv_growth / 100))) + (ar * (1 + (ar_growth / 100))) - (ap * (1 + (ap_growth / 100)))
    return nwc


# 2 ask user to enter the inv, ar and ap values (can be positive or negative) and print inv, ar, ap and nwc as float
inv_1 = float(input("Enter the current value of the inventory: "))
ar_1 = float(input("Enter the current value of the accounts receivable: "))
ap_1 = float(input("Enter the current value of the accounts payable: "))
nwc_begin = nwc_calc(inv_1,ar_1,ap_1)

print ("Your current inventory is {0}, accounts receivable {1} and accounts payable {2}".format(str(inv_1), str(ar_1),
                                                                                                str(ap_1)))
print ("Your current net working capital is {}".format(str(nwc_begin)))

# 3 ask user to enter growth percentages for next month without % sign, print new nwc and growth percentages

inv_var = float(input("Enter the next month inventory growth percentage without % sign (e.g. -1 or 4): "))
ar_var = float(input("Enter the next month accounts receivable growth percentage without % sign (e.g. -1 or 4): "))
ap_var = float(input("Enter the next month accounts payable growth percentage without % sign (e.g. -1 or 4): "))
nwc_forecast = nwc_calc(inv_1,ar_1,ap_1,inv_var, ar_var, ap_var)

print ("Your next month net working capital will be {}".format(str(nwc_forecast)))

print ("Inventory will have {0} %, accounts receivable {1} % and accounts payable {2} % growth in next month.".format(
                                                                                                        str(inv_var),
                                                                                                        str(ar_var),
                                                                                                        str(ap_var)))
# 4 give feedback to user

if nwc_forecast < 0:
    print("Good luck with that!")
if 0 < nwc_forecast < 100:
    print("Getting there, keep on going!")
if nwc_forecast > 100:
    print("Great job!")
