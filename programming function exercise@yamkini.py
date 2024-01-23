#QN1
"""def kilometer_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles
#Get user input
distance_in_kilometers = float(input("Enter distance in kilometers: "))
# Convert and display result
converted_distance =kilometer_to_miles(distance_in_kilometers)
print(f"{distance_in_kilometers} kilometers is equal to {converted_distance} miles.")"""

#QN2
"""# Sales Tax Program with Functions

def calculate_county_tax(purchase_amount):
    county_tax_rate = 0.02  # County sales tax rate (2%)
    return purchase_amount * county_tax_rate

def calculate_state_tax(purchase_amount):
    state_tax_rate = 0.04  #State sales tax rate (4%)
    return purchase_amount * state_tax_rate

def display_results(county_tax, state_tax, total_tax):
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")

# Get input from the user
purchase_amount = float(input("Enter the purchase amount: "))
# Calculate taxes using functions
county_tax = calculate_county_tax(purchase_amount)
state_tax = calculate_state_tax(purchase_amount)
total_tax = county_tax + state_tax
# Display results using a function
display_results(county_tax, state_tax, total_tax)"""

#QN3
"""def calculate_insurance(replacement_cost):
    # Minimum insurance recommended by financial experts is 80% of replacement cost
    minimum_insurance = 0.8 * replacement_cost
    return minimum_insurance
# Get input from the user
replacement_cost = float(input("Enter the replacement cost of the building: "))
# Calculate minimum insurance using the function
minimum_insurance = calculate_insurance(replacement_cost)
# Display the result
print(f"The minimum amount of insurance recommended is: ${minimum_insurance:.2f}")"""

#QN4
"""def calculate_total_expense(monthly_costs):
    total_monthly_cost = sum(monthly_costs)
    total_annual_cost = total_monthly_cost * 12
    return total_monthly_cost, total_annual_cost
# Get user input for monthly costs
loan_payment = float(input("Enter loan payment amount: "))
insurance = float(input("Enter insurance amount: "))
gas = float(input("Enter gas expense: "))
oil = float(input("Enter oil expense: "))
tires = float(input("Enter tires expense: "))
maintenance = float(input("Enter maintenance expense: "))
# Calculate total monthly and annual costs
monthly_costs = [loan_payment, insurance, gas, oil, tires, maintenance]
total_monthly, total_annual = calculate_total_expense(monthly_costs)
# Display results
print(f"\nTotal Monthly Cost: ${total_monthly:.2f}")
print(f"Total Annual Cost: ${total_annual:.2f}")"""

#QN5
"""def calculate_property_tax(actual_value):
    # Calculate assessment value (60% of actual value)
    assessment_value = 0.6 * actual_value
    # Calculate property tax (64¢ for each $100 of the assessment value)
    property_tax = (assessment_value / 100) * 0.64
    
    return assessment_value, property_tax
# Get user input for actual property value
actual_value = float(input("Enter the actual value of the property: $"))
# Calculate assessment value and property tax
assessment_value, tax_amount = calculate_property_tax(actual_value)
# Display results
print(f"\nAssessment Value: ${assessment_value:.2f}")
print(f"Property Tax: ${tax_amount:.2f}")"""

#QN6
"""def calculate_bmi(weight, height):
    # BMI formula: BMI = weight * 703 / height^2
    bmi = (weight * 703) / (height ** 2)
    return bmi
# Get user input for weight (in pounds) and height (in inches)
weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))
# Calculate BMI
bmi_result = calculate_bmi(weight, height)
# Display result
print(f"\nBody Mass Index (BMI): {bmi_result:.2f}")"""

#QN7
"""def calculate_calories_from_fat(fat_grams):
    # Calories from fat formula: calories = fat grams * 9
    calories_from_fat = fat_grams * 9
    return calories_from_fat

def calculate_calories_from_carbs(carb_grams):
    # Calories from carbs formula: calories = carb grams * 4
    calories_from_carbs = carb_grams * 4
    return calories_from_carbs
# Get user input for fat grams and carbohydrate grams
fat_grams = float(input("Enter the number of fat grams consumed: "))
carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))
#Calculate calories from fat and carbohydrates
calories_from_fat = calculate_calories_from_fat(fat_grams)
calories_from_carbs = calculate_calories_from_carbs(carb_grams)
# Display results
print(f"\nCalories from Fat: {calories_from_fat} calories")
print(f"Calories from Carbohydrates: {calories_from_carbs} calories")"""

#QN8
"""def calculate_income(class_a_tickets, class_b_tickets, class_c_tickets):
    # Ticket prices
    price_class_a = 15
    price_class_b = 12
    price_class_c = 9

# Calculate income from ticket sales
    income = (class_a_tickets * price_class_a) + (class_b_tickets * price_class_b) + (class_c_tickets * price_class_c)
    return income

# Get user input for the number of tickets sold for each class
class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

# Calculate total income
total_income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)

# Display results
print(f"\nTotal Income from Ticket Sales: ${total_income}")"""

#QN9
"""def paint_job_estimator(square_feet, paint_price_per_gallon):
# Constants
    square_feet_per_gallon = 115
    hours_of_labor_per_gallon = 8
    labor_hourly_rate = 20.00

# Calculate the number of gallons of paint required
    gallons_of_paint = square_feet / square_feet_per_gallon

# Calculate the hours of labor required
    hours_of_labor = gallons_of_paint * hours_of_labor_per_gallon

# Calculate the cost of paint
    paint_cost = gallons_of_paint * paint_price_per_gallon

# Calculate labor charges
    labor_charges = hours_of_labor * labor_hourly_rate

# Calculate the total cost of the paint job
    total_cost = paint_cost + labor_charges

    return gallons_of_paint, hours_of_labor, paint_cost, labor_charges, total_cost

# Get user input for square feet and paint price per gallon
square_feet_to_paint = float(input("Enter the square feet of wall space to be painted: "))
paint_price_per_gallon = float(input("Enter the price of paint per gallon: $"))

# Calculate and display results
gallons, hours, paint_cost, labor_charges, total_cost = paint_job_estimator(square_feet_to_paint, paint_price_per_gallon)

# Display results
print(f"\nNumber of Gallons of Paint Required: {gallons:.2f} gallons")
print(f"Hours of Labor Required: {hours:.2f} hours")
print(f"Cost of Paint: ${paint_cost:.2f}")
print(f"Labor Charges: ${labor_charges:.2f}")
print(f"Total Cost of the Paint Job: ${total_cost:.2f}")"""

#QN10
"""def calculate_sales_tax(total_sales):
# Sales tax rates
    state_tax_rate = 0.04  # 4%
    county_tax_rate = 0.02  # 2%

# Calculate the amount of county sales tax
    county_sales_tax = total_sales * county_tax_rate

# Calculate the amount of state sales tax
    state_sales_tax = total_sales * state_tax_rate

# Calculate the total sales tax
    total_sales_tax = county_sales_tax + state_sales_tax

    return county_sales_tax, state_sales_tax, total_sales_tax

# Get user input for total sales for the month
total_sales_for_month = float(input("Enter the total sales for the month: $"))

# Calculate and display results
county_tax, state_tax, total_tax = calculate_sales_tax(total_sales_for_month)

# Display results
print(f"\nAmount of County Sales Tax: ${county_tax:.2f}")
print(f"Amount of State Sales Tax: ${state_tax:.2f}")
print(f"Total Sales Tax (County plus State): ${total_tax:.2f}")"""