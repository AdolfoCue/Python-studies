Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def calcBills():
    myBills = {'Electric': 120.00, 'Rent': 1200.00, 'Water_Sewer': 60.00, 'Car_Insurance': 75.00, 'Phone': 65.00}
    total = 0
    for i in myBills:
        total += myBills[i]
    owed = 'The total owed for bills this month is: ${}'.format(total)
    return owed