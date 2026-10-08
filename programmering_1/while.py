"""
while True:
    svar = input("skriv 'exit' för att avsluta: ").lower()
    if svar == "exit":
        break
        """

"""
number = int(input("Ange ett tal: "))

count = 1
while count <= number:
    print(count)
    count = count + 1
    """
"""

secret = 5

while True:
    guess = int(input("Gissa numret (upp till 20): "))

    if guess < secret:
        print("För lågt!")
    elif guess > secret:
        print("För högt!")
    else:
        print("Grattis du gissade rätt!")
        break
        
        """


secret = "lösenord"


while True:
    guess = str(input("skriv i rätt lösernord ")) 

    if guess < secret:
        print ("Fel lösenord")
    else:
        print ("du gissa rätt")

        break