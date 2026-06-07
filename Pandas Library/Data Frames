import pandas as pd

#Creating a DataFrame with the help of list of lists and column names
Employee = pd.DataFrame([["Radha", 23,25000],
                        ["Krish", 25, 30000],
                        ["Shyam", 22, 75000],
                        ["Shiv",24, 50000],
                        ["Siya",25,80000],
                        ["Roshan", 26,450000]], columns=["Name", "Age", "salary"])

print("DataFrame:") 
print(Employee)         #Prints the DataFrame
print()

print("Employee Name: " + Employee["Name"][0])     #Prints the name of first employee
print()

print("Employee Name With Index: ")
print(Employee["Name"])   #Prints the name of all employees
print()

print("First 5 rows: ")
print(Employee.head())  #Prints the first 5 rows of the DataFrame
print()

print("Last 5 rows: ")
print(Employee.tail())   #Prints the last 5 rows of the DataFrame
print()

print("DataFrame Information:")   
print()          
Employee.info()                 #Prints the information about the DataFrame
print()

print("DataFrame Shape: " + str(Employee.shape))    #Prints the shape of the DataFrame
print()

print("Column Names: " + str(Employee.columns))     #Prints the column names of the DataFrame
print()

print("Index: " + str(Employee.index))              #Prints the index of the DataFrame
print()

print("Mean Salary: " + str(Employee.salary.mean()))        #Prints the mean salary of the employees
print()

print("Median Salary: " + str(Employee.salary.median()))     #Prints the median salary of the employees
print()

print("Mode salary: ")
print(Employee.salary.mode())           #Prints the mode salary of the employees
print()

print("Minimum Salary: " + str(Employee.salary.min()))          #Prints the minimum salary of the employees
print()

print("Maximum Salary: " + str(Employee.salary.max()))          #Prints the maximum salary of the employees
print()

print("Sum of Salaries: " + str(Employee.salary.sum()))     #Prints the sum of salaries of the employees
print()

print("Count of Salaries: " + str(Employee.salary.count()))    #Prints the count of salaries of the employees
print()

print("Standard Deviation of Salaries: " + str(Employee.salary.std()))      #Prints the standard deviation of salaries of the employees
print()

print("Variance of Salaries: " + str(Employee.salary.var()))           #Prints the variance of salaries of the employees
print()

print("25th Percentile of Salaries: " + str(Employee.salary.quantile(0.25)))            #Prints the 25th percentile of salaries of the employees
print()


