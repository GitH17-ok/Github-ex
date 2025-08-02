import json
import random

# Beispiel-Fragen
fragen = [
    {
        "frage": "Was ist die Hauptstadt von Frankreich?",
        "optionen": ["Berlin", "Madrid", "Paris", "Rom"],
        "richtig": 2
    },
    {
        "frage": "Welches Element hat das Symbol 'O'?",
        "optionen": ["Gold", "Sauerstoff", "Silber", "Wasserstoff"],
        "richtig": 1
    }
]

punkte = 0
random.shuffle(fragen)

for i, f in enumerate(fragen):
    print(f"\nFrage {i+1}: {f['frage']}")
    for idx, opt in enumerate(f['optionen']):
        print(f"  {idx+1}. {opt}")
    try:
        antwort = int(input("Deine Antwort (Zahl): ")) - 1
        if antwort == f['richtig']:
            print("✅ Richtig!")
            punkte += 1
        else:
            print(f"❌ Falsch! Richtig wäre: {f['optionen'][f['richtig']]}")
    except ValueError:
        print("❗ Ungültige Eingabe.")

print(f"\nDu hast {punkte} von {len(fragen)} richtig beantwortet.")