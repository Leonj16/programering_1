
"""
def hej(Niklas):
    print(f"Hej {Niklas}, Välkommen!")

Användarens_name = input("Vad heter du? ")
hej(Användarens_name)
"""
def beräkna_area(width, height):
    return width * height

bredd = float(input("Ange rektangelns bredd "))
höjd = float(input("Ange rektangelns höjd:"))

area = beräkna_area(bredd, höjd)
print(f"Rektangelns area är: {area}")