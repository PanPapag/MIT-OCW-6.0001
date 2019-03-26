annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal: "))

current_savings = 0
r = 0.04
portion_down_payment = 0.25
months_passed = 0

while(current_savings <= (portion_down_payment * total_cost) ):
    monthly_salary = annual_salary/12
    if months_passed%6==0 and months_passed!=0 :
        annual_salary += annual_salary * semi_annual_raise

    current_savings = current_savings + portion_saved * monthly_salary
    current_savings = current_savings + current_savings * r/12
    months_passed = months_passed + 1

print("Number of months: " + repr(months_passed))
