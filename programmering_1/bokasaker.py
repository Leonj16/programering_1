class Equipment:
    def __init__(self, name, category, available):
        self.name = name
        self.category = category
        self.available = available


equipment_list = [
    Equipment("Camera", "Camera", True),
    Equipment("PS5", "Gaming", True),
    Equipment("MacBook", "Computer", False),
    Equipment("Projector", "Video", True),
    Equipment("Speaker", "Audio", True)
]


def show_equipment():
    print("\nEquipment:")
    number = 1

    for item in equipment_list:
        print(number, item.name, item.available)
        number = number + 1


def book_equipment():
    show_equipment()
    number = int(input("Choose number: "))

    if number >= 1 and number <= len(equipment_list):
        item = equipment_list[number - 1]

        if item.available == True:
            item.available = False
            print("Equipment booked!")
        else:
            print("Already booked!")
    else:
        print("Wrong number!")


def return_equipment():
    show_equipment()
    number = int(input("Choose number: "))

    if number >= 1 and number <= len(equipment_list):
        item = equipment_list[number - 1]

        if item.available == False:
            item.available = True
            print("Equipment returned!")
        else:
            print("Not booked!")
    else:
        print("Wrong number!")


while True:
    print("\n1. Show equipment")
    print("2. Book equipment")
    print("3. Return equipment")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_equipment()

    elif choice == "2":
        book_equipment()

    elif choice == "3":
        return_equipment()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Wrong choice!")