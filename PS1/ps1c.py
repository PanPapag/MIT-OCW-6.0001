annual_salary = int(input("Enter the starting salary: "))

current_savings = 0
semi_annual_raise = 0.07
r = 0.04
down_payment_portion = 0.25
total_cost = 1000000
months = 36
diff = 5000
low = 0.00
high = 1.00
portion_guess = (low+high)/2
num_guesses = 0

while abs(current_savings - total_cost * down_payment_portion) >= diff and low < high:
    current_savings = 0
    temp_annual_salary = annual_salary

    for n in range(months+1):
        monthly_salary = temp_annual_salary/12
        if n % 6 == 0 and n != 0 :
            temp_annual_salary += temp_annual_salary * semi_annual_raise
        current_savings = current_savings + portion_guess * monthly_salary
        current_savings = current_savings + current_savings * r/12

    if current_savings < total_cost * down_payment_portion:
        low = portion_guess
    else:
        high = portion_guess

    portion_guess = (low+high)/2
    num_guesses += 1

if(low < high):
    print("Best saving rate: " + str(portion_guess))
    print("Steps in bisection search: " + str(num_guesses))
else:
    print("It is not possible to pay the down payment in three years.")
