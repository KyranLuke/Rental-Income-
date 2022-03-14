Income = float(input("Enter in all Monthly Income Combined: "))

Taxes = float(input("Enter In Monthly Taxes: "))
Insurance = float(input("Enter In Monthly Insurance: "))
Utilities = float(input("Enter In Monthly Utilities: "))
Hoa = float(input("Enter In Hoa if Apical: "))
Yard = float(input("Enter In Lawn or Snow care if Apical: "))
Morgage = float(input("Enter In Monthly Morgage: "))
Saving = float(input("Enter in how much you would like to save for Vaccancy, Repairs, Capex, and ect: "))

Expenses = Taxes + Insurance + Utilities + Hoa + Yard + Morgage + Saving

Down = float(input("Enter In Down Payment: "))
Closeing = float(input("Enter In CLosing Cost: "))
Rehab = float(input("Enter In Rehab Budget: "))
Ect = float(input("Enter In Any other costs: "))

Investments = Down + Closeing + Rehab + Ect

def Roi():
    cash_Flow = Income - Expenses
    Roi = (cash_Flow/Investments)* 100
    print(Roi)

Roi()