import random

def ask_question(question_data):
    print("\n" + question_data["question"])

    for alternative in question_data["alternatives"]:
        print(alternative)

    answer = input("Ditt svar: ").strip().lower()

    if answer == question_data["correct_answer"]:
        print("Rätt svar!")
        return 1
    else:
        print("Fel svar!")
        print("Rätt svar var:", question_data["correct_answer"])
        return 0


def calculate_grade(score, max_score):
    percentage = (score / max_score) * 100

    if percentage >= 90:
        return "Utmärkt!"
    elif percentage >= 70:
        return "Bra!"
    elif percentage >= 50:
        return "Godkänt!"
    else:
        return "Försök igen!"


player_name = input("Vad heter du? ").strip()

while player_name == "":
    print("Du måste skriva ett namn.")
    player_name = input("Vad heter du? ").strip()


questions = [
    {
        "question": "Vilken datatyp används för heltal i Python?",
        "alternatives": ["a) str", "b) int", "c) float"],
        "correct_answer": "b"
    },
    {
        "question": "Vilket kommando används för att skriva ut text?",
        "alternatives": ["a) print()", "b) input()", "c) random()"],
        "correct_answer": "a"
    },
    {
        "question": "Vilken loop används ofta när man vill gå igenom en lista?",
        "alternatives": ["a) if", "b) for", "c) def"],
        "correct_answer": "b"
    },
    {
        "question": "Vilket tecken används för att jämföra om två värden är lika?",
        "alternatives": ["a) =", "b) ==", "c) !="],
        "correct_answer": "b"
    },
    {
        "question": "Vilken funktion används för att ta reda på längden på en lista?",
        "alternatives": ["a) int()", "b) range()", "c) len()"],
        "correct_answer": "c"
    },
    {
        "question": "Vad betyder int?",
        "alternatives": ["a) Text", "b) Heltal", "c) Lista"],
        "correct_answer": "b"
    },
    {
        "question": "Vilket tecken används för att skriva en kommentar i Python?",
        "alternatives": ["a) #", "b) @", "c) $"],
        "correct_answer": "a"
    }
]

random.shuffle(questions)

score = 0
answered_questions = []

for question in questions:
    try:
        points = ask_question(question)
        score += points
        answered_questions.append(question["question"])
    except Exception:
        print("Något gick fel med frågan.")

max_score = len(questions)

result = {
    "name": player_name,
    "score": score,
    "max_score": max_score
}

print("\n-----------------------")
print("RESULTAT")
print("-----------------------")

print("Spelare:", result["name"])
print("Poäng:", result["score"], "/", result["max_score"])

message = calculate_grade(score, max_score)
print(message)

print(result["name"], "fick", result["score"], "av", result["max_score"], "poäng.")

print("\nDu svarade på följande frågor:")

question_number = 1

for question in answered_questions:
    print(question_number, "-", question)
    question_number += 1

print("\nTack för att du spelade!")

