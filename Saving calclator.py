save = int(input("How many dollars would you like to save in one year? "))

muny = str(save)

print("To save up $" + muny + " in one year you will need to save:")

month = round(save / 12,2)

week = round(save / 52,2)

day = round(save /365,2)


monthly = str(month)
weekly = str(week)
daily = str(day)


print("Monthly: " + monthly )
print("Weekly: " + weekly )
print("Daily: " + daily )
