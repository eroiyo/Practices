#just 2b and 2C
#hi there, can u help me with some questions?
# Question 2A (5K marks):
# Define a dictionary called “class grades” that has at least 10 key value pairs. Each key should be a student name, and each value should be a score that represents their average for their courses.


class_grades = {"Natalia": 95, "Sam": 67, "Lily": 99, "Bob": 57, "George": 78, "John": 86, "Mandy": 32, "Oliver": 89, "Winn": 45, "Victor": 92, "Candy": 83}

# Question 2B (4A marks):
# Print all the keys of your dictionary. Then, print all the values of your dictionary.

for x, y in class_grades.items():
  print(x, y)


# Question 2C (5T marks): iterate through your dictionary using For loop (as shown in slides) to add 5% to every student’s average. OPTIONAL: If you want an extra challenge, try to make sure their average does not go above 100.
print("-----------------")
for x,y in class_grades.items():
    class_grades[x]=y+5
    if(class_grades[x]>100):
        class_grades[x]=100


for x, y in class_grades.items():
  print(x, y)

      