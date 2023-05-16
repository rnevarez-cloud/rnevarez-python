print("Welcome!\n")

company_name = input("Please enter your company name: ")

feet_of_fiber = float(input("Please enter the feet of fiber optic cable: "))

if feet_of_fiber > 500:
  total_cost = feet_of_fiber * .5
elif feet_of_fiber > 250:
  total_cost = feet_of_fiber * .7
elif feet_of_fiber > 100:
  total_cost = feet_of_fiber * .8
else:
  total_cost = feet_of_fiber * .87

print("Company name: " + company_name)
print("Total cost: " + str(total_cost))
