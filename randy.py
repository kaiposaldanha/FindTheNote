import random

nota = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
corda = ["E", "A", "D", "G", "B", "e"]

notax = random.choice(nota)
cordax = random.choice(corda)

print(f"na corda {cordax}, encontre a nota {notax}")
