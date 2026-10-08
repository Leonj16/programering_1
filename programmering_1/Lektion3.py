"""
Points = float(input("Hur många poäng fick dom? (0-100)"))
if Points >= 90:
    print("Dom fick A.")
elif Points >= 80:
    print("Dom fick B.")
elif Points >= 70:
    print("Dom fick C.")
elif Points >= 60:
    print("Dom fick D.")
else:
    print("Dom fick F.")

"""
"""

Roll = input("vad är din roll? (admin,lärare eller elev?").lower()
if Roll == "admin":
    print("välkommen admin")
elif Roll == "lärare":
    print("välkommen lärare")
elif Roll == "elev":
    print("välkommen elev")
else:
    print("ogiltig roll")
"""
"""

password = (input("vad är ditt lösenord?"))

if len(password) < 6:
    print("lösenordet är för kort")
elif len(password) <= 10:
    print("lösenordet är godkänt")
else:
    print("lösenordet är starkt")


"""
name = input("vad heter du? ")
Age = int(input("hur gammal är du? "))

Current_year = 2026
year_turning_100 = Current_year - Age + 100
print(f"Hej {name}, du kommer att fylla 100 år år {year_turning_100}")


"""
Age = int(input("hur gammal är du? "))
Student = input("Är du student? (ja/nej): ").lower()
if Age < 12:
    print("pris = 50")
elif Age <= 17:
   print("pris = 80kr")
elif Age >= 18 and Student == "ja":
    print("pris = 100kr")
else:
   print("pris = 150kr")
   """