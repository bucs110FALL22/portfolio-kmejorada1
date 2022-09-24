import random
#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = ((cost_per_week)/(classes_per_week))
print(cost_per_class, type(cost_per_class))
#Part B
list = [17, 7, 27, 21, 44]
choice = random.choice(list)
print(choice, type(choice))