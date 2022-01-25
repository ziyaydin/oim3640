# ex02-1
# What is the volume of a sphere with radius 5?

r=5
pi=3.141592653589793
print("The volume of a sphere with radius 5:", 4/3 * pi * r * r * r )

#ex02-2
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cp= 24.95 * 0.6 #discounted cover price of the book
fcsc = 3 #first copy shipping cost is $3
fctc = cp + fcsc #first copy total cost
acsc = 0.75 #additional copy shipping cost
ac = 59 #number of additional copies
actc = (cp * ac) + (acsc * ac) #additional copy total cost
print("Total wholesale cost of 60 copies is:", fctc + actc)

#ex02-3
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

eptt = ((8 + 15/60)/60) * 2 #easy pace total time
ttt = ((7 + 12/60)/60) * 3 #tempo total time
gttt = eptt + ttt #grand total total time in minutes
print("Total running time is", gttt, "hours") #total running time its 37 minutes and 66 seconds (38 minutes and 6 seconds)
st = (6 + 52/60)
print( st + gttt)
bt = ("7", + 0.5 * 60) #breakfast time
print("I can eat my breakfast at 7.30 AM")

#exp02-4
#If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as xx.x%. Keep one figure after decimal point.
ng = 89 #new grade
og = 82 #old grade
increase = ((ng-og)/og)
percentage = f"{increase:.1%}"
print(percentage)
print("My grade would increased by", percentage)