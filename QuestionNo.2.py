#To compute a person's income tax, where the unit of the gross income, standard deduction, income tax and dependent deduction are in dollars($)
Gross_income = int(input("Enter the value of Gross income: "))
No_of_Dependents = int(input("Enter the value of Number of dependents: "))
Standard_Deduction = 10000 
Dependent_Deduction = 3000
Income_Tax = Gross_income - Standard_Deduction - ( Dependent_Deduction*No_of_Dependents ) #Because each dependent has a deduction value of 3,000

print("The value of income tax is: ", Income_Tax)
