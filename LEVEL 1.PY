# DECISION MAKING OR CONDITONAL OPERATORS 
# USE TO CHECK THE WHETHER CONDITON ARE TRUE OR FALSE







 # IF - USE TO ONLY SINGLE CONDITION WITH SINGLE - OR NO OUTPUT

# SYNTAX : 

#  if condition:

    # code if condition is True

# EXAMPLE : 


age = int(input("ENTER AGE : "))

if age < 18 :

    print("YOU ARE NOT ADULT ")








# IF - ELSE

# WHAT IS IF-ELSE  : It lets your program make decisions based on conditions — just like your brain does.

# EXAMPLE : If it’s raining → take an umbrella ☂️         Else → go freely 🌞

# SYNTAX :

#  if condition:

    # code if condition is True

#else:

    # code if condition is False

#  EXAMPLE :-

age = int(input("\nENTER YOU AGE : "))

if age >= 18 :    # YOU CAN WRIET LIKE THIS TOO : if( age >= 18 ) :

    print("YOU ARE ELIGIBLE FOR DRIVING LICENCE /n")

else:
    print("YOU HAVE TO WAIT MORE" , 18 - age ," YEARS FOR APPLYING DRIVING LICENCE !")








# if - elif - else 

# WHAT IS IF - ELSI - ELIF : IT IS USED TO CHECK MULTIPLE CONDITIONS 

# SYNTAX : 


#  if condition:

    # code if condition is True

# elif condition :

    # code if condition is true

#else:

    # code if condition is False

# EXAMPLE :

marks = int(input("\nENTER YOUR MARKS : "))

if marks < 35 :
    print("YOU ARE FAILED ! ")


elif marks < 60 :
    print("YOU ARE AVERAGE .")


elif  marks < 80 :
    print("YOU ARE GOOD CAN BE IMPROVED EASILY ")


else:
    print("YOU ARE BEST ! ")


# When there are multiple conditions, use elif (else if):

#Python uses indentation (spaces) to define blocks — no {} like C.
#→ Always use 4 spaces or 1 Tab after if, elif, else:

#Conditions can be combined: USING ( LOGICAL OPERATORS : OR , AND , NOT )



# THESE STATEMENT CAN BE USED WITH LOGICAL OPERATORS 

#EXAMPLE :  
 
age_1 = int(input("\nENTER YOUR AGE : "))

if age_1 > 18 and age_1 < 40 :
    print("YOU ARE YOUNG !")

else : 
    print("YOU ARE NOT YOUNG")









STUDENT =  input("\nARE YOU STUDENT (Y/N) : ")
DISCOUNT = input("YOU HAVE AN DISCOUNT COUPEN Y/N) : ")


if STUDENT == "Y" or DISCOUNT == "Y" :
    print("YOU WILL GET 50% DISCOUNT !")

else : 
    print("YOU HAVE TO PAY 100% AMOUNT ! ")










not_raining = input("\nIS IT RANING ( Y/N ) :")

if not not_raining == "Y" :                 # NOT OPERATOR 

    print("GO WITOHUT AN AMBRELLA ")

else : 

    print("GET AN UMBRELLA !")















# IF - ELIF - ELSE LADDER 



name = input("\nENTER YOR NAME  : ")
branch = input("ENTER YOR BRANCH : ")

if name == "rudra":
    if branch == "IT" :
        print("WELCOME RUDRA ! ")

else :
    print("YOU ARE NOT RUDRA ")

    