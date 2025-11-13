# Daily Calorie Tracker
print("Welcome to Daily Calorie Tracker!")

meals = []
calories = []
#Empty list in the start

# Ask number of meals
n = int(input("How many meals did you have today? "))

# Take meal names and calories
for i in range(n): #i is number entered in n to cont the loop
    meal = input(f"Enter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

# Calculate total and average calories
total = sum(calories)
average = total / n

# Ask daily limit
limit = float(input("Enter your daily calorie limit: "))

# Compare total with limit
if total > limit:
    print("You exceeded your daily calorie limit, STOPPP~!!!")
else:
    print("You are within your daily calorie limit, GOOD GOING!!!")

# Display report
print("MEAL NAME-->CALORIES")
print("-----------------------------")
for i in range(n):
    print(f"{meals[i]}--->{calories[i]}")
print(f"Total:--->{total}")
print(f"Average:{average:}")
#{} for strings to appear
print("THANK YOU FOR USING CALORIE TRACKER APP!!!STAYY HEALTHY")