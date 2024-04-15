import matplotlib.pyplot as plt

# define days of the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# initalizes empty list for storing daily calorie intake
calories_intake = []

# prompts user tp input their calorie intake for the day
for day in days:
    calories = int(input("Enter your calories for the day: "))
    calories_intake.append(calories)

# create the bar chart
plt.figure(figsize=(10, 6,))
plt.bar(days, calories_intake, color='skyblue')

# add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Calories Intake')
plt.title('Calories Intake per Day of the Week')

# show the plot
plt.xticks(rotation=45) #rotates x-axis labels for improved readability 
plt.tight_layout # adjusts layout to prevent labels clipping
plt.show()