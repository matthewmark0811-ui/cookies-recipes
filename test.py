#customer's input
customer = input("Enter customer name:")
numb_burgers = int(input("How many burgers are you ordering?"))
weight_beef = float(input("Enter weight of beef patty per burger (in grams):"))
cheese = int(input("Enter number of cheese slices per burger:"))
sauce = int(input("Enter tablespoon of sauce per burger:"))

#individual calories for each ingredient
beef_calories = 2.50*weight_beef
cheese_calories = 70.00*cheese
sauce_calories = 60.00*sauce
bun_calories = 150.00

#total calories for a single burger
total_calories_single = beef_calories + cheese_calories + sauce_calories + bun_calories

#grand total calories
total_grand_calories = total_calories_single*numb_burgers

#percentage calories contribution for each ingredient
beef_percentage = (beef_calories/total_calories_single)*100
cheese_percentage = (cheese_calories/total_calories_single)*100
sauce_percentage = (sauce_calories/total_calories_single)*100
bun_percentage = (bun_calories/total_calories_single)*100

#individual ingredient cost per burger
beef_cost = 0.04*weight_beef
cheese_cost = 1.00*cheese
sauce_cost = 0.50*sauce
bun_cost = 2.00

#total cost for a single burger
total_cost_single = beef_cost + cheese_cost + sauce_cost + bun_cost

#final cost for the whole burgers
final_cost = total_cost_single*numb_burgers

#display 
print("=============================================================================")
print("                      FOODSQUAT BURGER NUTRITION & COST                      ")
print("=============================================================================")

print("customer name :" , customer)
print("quantity of burger:" , numb_burgers)

print("-----------------------------------------------------------------------------")
print("CALORIES & COST BREAKDOWN (per burger):")

print(f"- Bun Base:        {bun_calories:.2f} kcal ({bun_percentage:.2f}%)   |   RM {bun_cost:.2f}")
print(f"- Beef Patty:      {beef_calories:.2f} kcal ({beef_percentage:.2f}%)   |   RM {beef_cost:.2f} ({weight_beef:.2f}g)")
print(f"- Cheese Slices:   {cheese_calories:.2f} kcal ({cheese_percentage:.2f}%)   |   RM {cheese_cost:.2f} ({cheese} slice/s)")
print(f"- Extra Sauce:     {sauce_calories:.2f} kcal ({sauce_percentage:.2f}%)   |   RM {sauce_cost:.2f} ({sauce:.2f} tbsp)")

print("----------------------------------------------------------------------------")
print(f"TOTAL EACH BURGER:    {total_calories_single:.2f} kcal         |   RM {total_cost_single:.2f}")
print("----------------------------------------------------------------------------")

print(f"GRAND TOTAL CALORIES: {total_grand_calories:.2f} kcal ")
print(f"TOTAL MENU COST:                          |   RM {final_cost:.2f}")

print("============================================================================")

print("                      Eat Wisely for Healthy Living!                        ")

print("============================================================================")
