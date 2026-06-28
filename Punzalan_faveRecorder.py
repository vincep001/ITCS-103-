import openpyxl as op
import  datetime 


wbk = op.Workbook()
sheet = wbk.active


sheet['A1'] = "ID" 
sheet['B1'] = "First Name"
sheet['C1'] = "Last Name"
sheet['D1'] = "Birth Year"
sheet['E1'] = "Age"


calcu_year = datetime.datetime.now().year



#1

print("\nPerson 1")
first_name1 = input("Enter first name: ")
Last_name1 = input("Enter last name: ")
birth_year1 = int(input("Enter birth year: "))

age1 = calcu_year - birth_year1

sheet['A2'] = 1
sheet['B2'] = first_name1
sheet['C2'] = Last_name1
sheet['D2'] = birth_year1
sheet['E2'] = age1

#2nd

print("\nPerson 2")
first_name2 = input("Enter first name: ")
Last_name2 = input("Enter last name: ")
birth_year2 = int(input("Enter birth year: "))

age2 = calcu_year - birth_year2


sheet['A3'] = 2
sheet['B3'] = first_name2
sheet['C3'] = Last_name2
sheet['D3'] = birth_year2
sheet['E3'] = age2




#3rd
print("\nPerson 3")
first_name3 = input("Enter first name: ")
Last_name3 = input("Enter last name: ")
birth_year3 = int(input("Enter birth year: "))

age3 = calcu_year - birth_year3

sheet['A4'] = 3
sheet['B4'] = first_name3
sheet['C4'] = Last_name3
sheet['D4'] = birth_year3
sheet['E4'] = age3







#saving the file
wbk.save("favorite_people.xlsx")

print("Favorite people saved successfully!")
print("=== FAVORITE PEOPLE LIST ===")

for rows in sheet.iter_rows(values_only=True):
    print(rows)

print("Press Enter to exit...")