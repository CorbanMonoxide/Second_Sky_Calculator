'''
Secret Sky 2021 Cost Calculator
September 18 + 19 2021
Cesar E. Chavez Park - Berkley, CA
'''

'''VARIABLES'''

days = 2 #Total days in the hotel
people = 8 #Total number of people accounted for

'''The Basics'''
plane = 313 #plane ticket price
plane_total = plane * (people - 2) #total price of all plane tickets
concert = 150 #concert ticket price
concert_total = concert * people #Total price of Concert Tickets
Air_Bnb_Per_Person = 144 #hotel price per night per person
Air_Bnb_Total = Air_Bnb_Per_Person * people #Total Cost of Air BNB

'''Extras'''

food = 120 #food budget
merch = 120 #merch budget
weed = 120 #Weed Budget
uber = 100 #Uber Budget
emergency_fund = 200 #emergency fund

'''TOTALS'''

Upfront_Total = plane_total + Air_Bnb_Total + concert_total # Upfront Total Cost

Base_Total = plane + concert + Air_Bnb_Per_Person #Total Base Cost
Reccomended_Base_Total = Base_Total + merch + food
Florida_Friend_Total = Base_Total - plane

Bobbie_Total =Base_Total + food + merch #Bobbie's Total
Calyx_Total = Base_Total #Calyx's Total
Collyn_Total = Florida_Friend_Total #Collyn's Total
Corban_Total = Base_Total + food + merch + weed + uber + emergency_fund #Corban's Total
Jacob_Total = Base_Total #Jacob's Total
Keegan_Total = Base_Total #Keegan's Total
Tommy_Total = Florida_Friend_Total # Tommy's Total
Zoe_Total = Base_Total #Zoe's Total


Grand_Total = (Base_Total * 6) + (Florida_Friend_Total * 2) #Grand Total

Reccomended_Grand_Total = (Reccomended_Base_Total * 6) + (Florida_Friend_Total * 2)

'''AMOUNT PAID'''

Bobbie_Payment = 0
Calyx_Payment = 0
Collyn_Payment = 150 #Collyn's Payment as of 5/6/2021
Corban_Payment = 0
Jacob_Payment = 0
Keegan_Payment = 0
Tommy_Payment = 150 #Tommy's Payment as of 5/6/2021
Zoe_Payment = 0


Paid_Total = Bobbie_Payment + Calyx_Payment + Corban_Payment + Jacob_Payment + Keegan_Payment + Zoe_Payment

'''OUTPUT'''

print("Second Sky 2021 Budget")
print("\n-----------------------------------\n")
print("###Cost Totals###" + '\n')


print("Air BNB cost: " + str(Air_Bnb_Total))
print("Air BNB cost per person: " + str(Air_Bnb_Per_Person))


print("Ticket cost: " + str(concert_total))
print("Ticket cost per person: " + str(concert))
print("Plane ticket Cost: " + str(plane_total))
print("Plane ticket cost per person: " + str(plane) + '\n')
print("Upfront Cost: " + str(Upfront_Total))
print("\n-----------------------------------\n")
print("###Individual Cost Totals###" + '\n')
print("Base Cost (Plane,Concert Ticket,Air BNB): " + str(Base_Total))
print("Base Cost For Friends From Flordia (Concert + Air BNB): " + str(Florida_Friend_Total) + '\n')
print("Reccomended Food Budget: " + str(food))
print("Reccomended Merch Budget: " + str(merch) + '\n')
print("Base Cost Including Recommended Budgets: " +str(Reccomended_Base_Total))

print("Individual Cost Below" + '\n')
print("Bobbie's Estimated Cost: " + str(Bobbie_Total))
print("----- Amount Paid: " + str(Bobbie_Payment)) 
print("Calyx's Estimated Cost: " + str(Calyx_Total))
print("----- Amount Paid: " + str(Calyx_Payment)) 
print("Collyn's Estimated Cost: " + str(Collyn_Total))
print("----- Amount Paid: " + str(Collyn_Payment))
print("Corban's Estimated Cost: " + str(Corban_Total))
print("----- Amount Paid: " + str(Corban_Payment)) 
print("Jacob's Estimated Cost: " + str(Jacob_Total))
print("----- Amount Paid: " + str(Jacob_Payment)) 
print("Keegan's Estimated Cost: " + str(Keegan_Total))
print("----- Amount Paid: " + str(Keegan_Payment)) 
print("Tommy's Estimated Cost: " + str(Tommy_Total))
print("----- Amount Paid: " + str(Tommy_Payment))
print("Zoe's Estimated Cost: " + str(Zoe_Total))
print("----- Amount Paid: " + str(Zoe_Payment) + '\n')

print("Grand Total: " + str(Grand_Total))
print("Grand Total with extra budgets: " + str(Reccomended_Grand_Total))

