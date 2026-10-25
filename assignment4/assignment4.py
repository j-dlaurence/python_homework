# J-D Laurence

# Task 1
import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
#1
df = pd.DataFrame(data)
print(df)
task1_data_frame = df

#2
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

#3
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print(task1_older)

#4
task1_older.to_csv("employees.csv", index=False)

