# ex02-1
# What is the volume of a sphere with radius 5?

r = 5
pi = 3.141592653589793
print(f'The volume of a sphere with radius 5: {4/3 * pi * r * r * r:.2f}')

# ex02-2
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cover_price = 24.95 * 0.6  # discounted cover price of the book
first_copy_shipping_cost = 3  # first copy shipping cost is $3
first_copy_total_cost = cover_price + \
    first_copy_shipping_cost  # first copy total cost
additional_copy_shipping_cost = 0.75  # additional copy shipping cost
additonal_copies = 59  # number of additional copies
additional_copy_total_cost = (cover_price * additonal_copies) + (
    additional_copy_shipping_cost * additonal_copies)  # additional copy total cost
total_cost = first_copy_total_cost + additional_copy_total_cost
print(f'Total wholesale cost of 60 copies is: ${total_cost:.2f}')

# ex02-3
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

eptt = ((8 + 15/60)/60) * 2  # easy pace total time
ttt = ((7 + 12/60)/60) * 3  # tempo total time
gttt = eptt + ttt  # grand total total time in minutes
# total running time its 37 minutes and 66 seconds (38 minutes and 6 seconds)
print(f'Total running time is {gttt:.2f} hours')
st = (6 + 52/60)
print(st + gttt)
bt = ("7", + 0.5 * 60)  # breakfast time
print("I can eat my breakfast at 7.30 AM")

# exp02-4
# If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as xx.x%. Keep one figure after decimal point.
new_grade = 89  # new grade
old_grade = 82  # old grade
increase = ((new_grade-old_grade)/old_grade)
percentage = f"{increase:.1%}"
print(percentage)
print("My grade would increase by", percentage)

# End
