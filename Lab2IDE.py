'''
Will Anderson
8/31/2023

Change age to dog, cat, and horse years
'''

human_age = float(input("Enter your age: "))
dog_age = human_age * 7
dog_years = dog_age // 1 
# this gives us the quotient of years
dog_months = ((dog_age % 1) * 12) // 1 
# we now use the remainder of years * 12 to calculate months
# we still need the quotient of months to prevent getting a fraction
dog_days = ((dog_age % 1) * 12) % 1 * 30 // 1
# same idea as months but use remainder of months * 30, because 30 per month, to calc days

print("Your age in dog years is", dog_years, "years", dog_months, "months", dog_days, "days.")

cat_age = human_age / 9
# converts human age into cat age
cat_years = cat_age // 1
cat_months = ((cat_age % 1) * 12) // 1
cat_days = ((cat_age % 1) * 12) % 1 * 30 // 1
# after making the new adjustment from human_age -> cat_age, the rest of the formulas are the same

print("Your age in cat years is", cat_years, "years", cat_months, "months", cat_days, "days.")

horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
# converts human age into horse age
horse_years = horse_age // 1
horse_months = ((horse_age % 1) * 12) // 1
horse_days = ((horse_age % 1) * 12) % 1 * 30 // 1
# after converting human age to horse age, the rest of the formulas can be the same

print("Your age in horse years is", horse_years, "years", horse_months, "months", horse_days, "days.")
