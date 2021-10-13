#Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. #Using a formula that estimates a person’s yearly insurance costs, you will investigate how different factors such as age, sex, BMI, etc. affect the prediction.

# create the initial variables below
age = 35
smoker = 1
sex = 1
bmi = 27.3
num_of_children = 2 
# After the declaration of the variables, create a variable called insurance_cost that utilizes the following formula:

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

####Looking at Age Factor
# Age Factor
age +=4
print(age) # This will output 6 in the terminal
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's new insurance cost is " + str(new_insurance_cost) + " dollars.")

#difference between old and new insurance
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is  " + str(change_in_insurance_cost)+ " dollars.")
