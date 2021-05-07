'''
Secret Sky 2021 Cost Calculator
September 18 + 19 2021
Cesar E. Chavez Park - Berkley, CA
'''

'''VARIABLES'''

days = 2 #Total days in the hotel
people = 6 #Total number of people accounted for


plane = 313 #plane ticket price
plane_total = plane * people #total price of all plane tickets
concert = 150 #concert ticket price
concert_total = concert * people #Total price of Concert Tickets
hotel = 134 #hotel price per night per person
hotel_rooms = 3
hotel_total = hotel * days #Total hotel cost per days
hotel_grand = hotel * days * hotel_rooms #Grand total hotel cost.
concert_hotel = concert_total + hotel_grand #Total cost of concert and hotel
food = 100 #food budget
merch = 100 #merch budget
weed = 120 #Weed Budget
uber = 100 #Uber Budget
emergency_fund = 200 #emergency fund

'''TOTALS'''

Upfront_Total = plane_total + hotel_grand + concert_total # Upfront Total Cost

Base_Total = plane + concert + hotel

Bobbie_Total = plane + concert + (hotel_total / 2) + food + merch #Bobbie's Total
Calyx_Total = plane + concert + (hotel_total / 2) + food + merch #Calyx's Total
Corban_Total = plane + concert + (hotel_total / 2) + food + merch + weed + uber + emergency_fund #Corban's Total
Jacob_Total = plane + concert + (hotel_total / 2) + food + merch #Jacob's Total
Keegan_Total = plane + concert + (hotel_total / 2) + food + merch #Keegan's Total
Zoe_Total = plane + concert + (hotel_total / 2) + food + merch #Zoe's Total

Grand_Total = Bobbie_Total + Calyx_Total + Corban_Total + Jacob_Total + Zoe_Total #Grand Total

'''AMOUNT PAID'''

Bobbie_Payment = ''
Calyx_Payment = ''
Corban_Payment = ''
Jacob_Payment = ''
Keegan_Payment = ''
Zoe_Payment = ''
Collyn_Payment = ''

Paid_Total = Bobbie_Payment + Calyx_Payment + Corban_Payment + Jacob_Payment + Keegan_Payment + Zoe_Payment

'''OUTPUT'''

print("Second Sky 2021 Budget")
print("\n-----------------------------------\n")
print("###Cost Totals###" + '\n')


print("Hotel cost: " + str(hotel_grand))
print("Hotel cost per person: " + str(hotel))


print("Ticket cost: " + str(concert_total))
print("Ticket cost per person: " + str(concert))
print("Plane ticket Cost: " + str(plane_total))
print("Plane ticket cost per person: " + str(plane) + '\n')
print("Upfront Cost: " + str(Upfront_Total))
print("Upfront Cost Minus Plane Tickets: " + str(concert_hotel))
print("\n-----------------------------------\n")
print("###Individual Cost Totals###" + '\n')
print("Base Cost (Plane,Concert Ticket,Hotel): " + str(Base_Total))
print("Food Budget: " + str(food))
print("Merch Budget: " + str(merch) + '\n')

print("Cost totals below include food and merch:" + '\n')
print("Bobbie's Estimated Cost: " + str(Bobbie_Total))
print("----- Amount Paid: " + str(Bobbie_Payment)) 
print("Calyx's Estimated Cost: " + str(Calyx_Total))
print("----- Amount Paid: " + str(Calyx_Payment)) 
print("Corban's Estimated Cost: " + str(Corban_Total))
print("----- Amount Paid: " + str(Corban_Payment)) 
print("Jacob's Estimated Cost: " + str(Jacob_Total))
print("----- Amount Paid: " + str(Jacob_Payment)) 
print("Keegan's Estimated Cost: " + str(Keegan_Total))
print("----- Amount Paid: " + str(Keegan_Payment)) 
print("Zoe's Estimated Cost: " + str(Zoe_Total))
print("----- Amount Paid: " + str(Zoe_Payment) + '\n')

print("Grand Total: " + str(Grand_Total))


