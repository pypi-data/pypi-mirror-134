import csv
import random
import os
import pathlib

def load_codex():
    symbols_list = []
    path = pathlib.Path(str(__file__))
    path = path.parent
    path = os.path.join(path, os.path.join('data', 'periodictable.csv'))
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            symbols_list.append(row['Symbol'])

    codex = {}

    for key, value in enumerate(symbols_list):
        for pos, character in enumerate(value.lower()):
            if character not in codex.keys():
                codex[character] = [f"{key+1}:{pos+1}"]
            else:
                codex[character].append(f"{key+1}:{pos+1}")
    return codex

def encrypt(str):
    codex = load_codex()
    encrypted_str = ""
    for character in str:
        encrypted_str += random.choice(codex[character.lower()])
        encrypted_str += " "
    return encrypted_str