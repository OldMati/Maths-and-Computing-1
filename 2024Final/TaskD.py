# 02730341

# initiate the arrays storing serious and very serious crimes:
serious = []
v_serious = []

# loop until break
while True:
    # read the level of crime and save as an integer
    crime_lvl = int(input('The level of the crime:'))

    # if user input 0, break the loop
    if crime_lvl == 0:
        break
    
    # add crime to serious array if serious
    if crime_lvl >= 7:
        serious.append(crime_lvl)

    # add crime to very serious array if very serious
    if crime_lvl > 16:
        v_serious.append(crime_lvl)

# print the results
print('The average level of serious crimes:', sum(serious) / len(serious))
print('Number of very serious crimes:', len(v_serious))
