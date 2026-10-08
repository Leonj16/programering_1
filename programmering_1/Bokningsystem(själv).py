name = input("vad heter du? ")
age = int(input("hur gammal är du? (1-99) "))

Student = input("Är du student? (ja/nej) ")
Student = Student.lower()
people = int(input("hur många personer gäller bokningen?"))

print("Välj aktivitet.")
print("1. Bowling")
print("2. Lasertag")
print("3. Escape Room")

choice = int(input("välj aktivitet (1-3): "))

if choice == 1:
    activity = "Bowling"
    price = 120
elif choice == 2:
    activity = "Lasertag"
    price = 180
else:
    activity = "Escape Room"
    price = 250

total = price * people #räknar ut priset dvs om 3 bowling 120 ggr 3

if Student == "ja":
    total = total *0.90
    print("Du får 10% studentrabatt!")
elif Student != "ja":
    print("Ingen student rabbat.")
if age < 18:
    total = total *0.85
    print("Du får 15% Ungdomsrabatt!")
if people >= 5:
    total = total * 0.9
    print("Ni får 10% grupprabbat!")

is_vip = False
vip = input ("har du en VIP-kod? ")
if vip.upper() == "PYTHON":
    is_vip = True
    total = total - 50
    print("vip-koden är godkänd!")

if choice == 3 and age < 13:
    print("Du måste vara minst 13 år för att boka Escape room")
else:
   print("----- BOKNINGSBEKRÄFTELSE -----")
   print("Namn", name)
   print("Ålder", age)
   print("Aktivitet", activity)
   print("Antal personer", people)
   print("grundpris:", price * people, "kr")
   print("slutpris", total, "kr")
   if is_vip:
       print("vip-kund: ja")
   else:
       print("vip-kund: nej")
       print("Tack för din bokning!")