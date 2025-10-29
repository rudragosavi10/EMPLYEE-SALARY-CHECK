#  A SPECIAL PROJECT TO GET INPUT FROM EMPLOYEE TO CHECK THEY DESRVED MORE SALARY OR NOT 

print("\nWELCOME ! TO EMPLOYEE SALARY INCREASE FESTIVAL !")
print("FILL ALL INFORMATION IN WHETHER NUMBER OR CAPITAL LETTER !\n")


emp_name = input("ENTER YOUR NAME (FIRST AND LAST NAME ) : ")
emp_experiance = int(input("ENTER EXPERIENCE ( IN YEARS ) :"))
emp_salary = float(input("ENTER YOUR SALARY : "))
emp_branch = input("ENTER YOUR BRANCH : ")
emp_age = int(input("ENTER YOU AGE  : "))


if emp_experiance >= 12 :
    print("\nCONGRATS ! YOU HAVE +5000 SALARY ")
    new_sal = emp_salary + 5000

elif emp_experiance < 12 and emp_experiance >= 5 :
    print("\nCONGRATS ! YOU HAVE +3000 SALARY ")
    new_sal = emp_salary + 3000

elif emp_experiance > 4 and emp_experiance < 2 :
    print("\nCONGRATS ! YOU HAVE +1500 SALARY ")
    new_sal = emp_salary + 1500

elif emp_experiance < 2 :
    print("\nSORRY YOU DON'T HAVE ENOUGH EXPERIANCE ! STAY CONSISTENT YOY WILL REACH IT SOON ")
    new_sal = emp_salary


print("\nTHANK YOU FOR WORKING WITH US ! KEEP GROWING MR/MS.",emp_name)
print("YOU ARE DETAILS ( AS NEW RECOEDS ! ) ")

print("\n---------------------------------------------")
print(f"NAME        : {emp_name}")
print(f"AGE         : {emp_age} YEARS OLD ")
print(f"EXPERIANCE  : {emp_experiance} YEARS OF EXPERIANCE")
print(f"BRNACH      : {emp_branch} BRANCH")
print(f"\nOLD SALARY : ${emp_salary}")
print(f"NEW SALARY  : ${new_sal}")

print("\n>>>>>>>>>>>>>>>>>>> THANK YOU <<<<<<<<<<<<<<<<<<<<<<")

