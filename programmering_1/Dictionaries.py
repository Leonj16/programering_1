"""
student = {
    "name": "Leon",
    "age": 16,
    "program": "El- och energiprogramet"
}
print(student["name"])
"""
"""
car = {
    "brand": "Volvo",
    "year": 2023,
    "model": "xc70"

}

car["year"] = 2020

car["color"] = "Black"
car.pop("year")
print(car)

"""
"""
person = {}

person["name"] = input("Vad heter du? ")
person["age"] = input("Hur gammal är du? ")

print(person)

"""
student = {
    "name": "Leon",
    "age": 16,
    "program": "El- och energiprogramet"
}

for value in student.items():
    print(value)