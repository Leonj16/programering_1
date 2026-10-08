name = input("Vad heter du? ")
age = int(input("Hur gammal är du? "))

student = input("Är du student? (ja/nej): ")
student = student.lower()

people = int(input("Hur många personer gäller bokningen? "))

print("\nVälj aktivitet:")
print("1. Bowling - 120 kr/person")
print("2. Lasertag - 180 kr/person")
print("3. Escape room - 250 kr/person")

choice = int(input("Välj aktivitet (1-3): "))

if choice == 1:
    activity = "Bowling"
    price = 120
elif choice == 2:
    activity = "Lasertag"
    price = 180
else:
    activity = "Escape room"
    price = 250

total = price * people

if student == "ja":
    total = total * 0.90
    print("Du får 10% studentrabatt!")
elif student != "ja":
    print("Ingen studentrabatt.")

if age < 18:
    total = total * 0.85
    print("Du får 15% ungdomsrabatt!")

if people >= 5:
    total = total * 0.90
    print("Du får 10% grupprabatt!")

is_vip = False

vip = input("Har du en VIP-kod? ")

if vip.upper() == "PYTHON":
    is_vip = True
    total = total - 50
    print("VIP-koden är godkänd!")

if choice == 3 and age < 13:
    print("Du måste vara minst 13 år för att boka Escape room.")
else:
    price_per_person_after_discount = total / people

    print("\n----- BOKNINGSBEKRÄFTELSE -----")
    print("Namn: " + name)
    print("Ålder:", age)
    print("Aktivitet:", activity)
    print("Antal personer:", people)
    print("Grundpris:", price * people, "kr")
    print("Slutpris:", total, "kr")
    print("Pris per person efter rabatt:", price_per_person_after_discount, "kr")

    if is_vip:
        print("VIP-kund: Ja")
    else:
        print("VIP-kund: Nej")

    print("Tack för din bokning!")
