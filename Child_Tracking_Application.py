import pandas as pd

while True:

  print("Child Healthcare Tracking Application")
  print("Data Entry Form(1)")
  print("Data analysis results(2)")
  print("Exit(3)")

  Input = int(input("Please select an option: "))

  if Input == 1:
    
    print("Data Entry Form")
    print("Please enter the following information:")

    Name = (input("Child name:\n"))
    Gender =(input("Child gender:\n"))
    Age = (input("Child age:\n"))

  elif Input == 2:
    print("Data Analysis Results")

  elif Input == 3:
    break


data = {
'Name': [Name],
'Gender': [Gender],
'Age': [Age],


}

df = pd.DataFrame(data)

