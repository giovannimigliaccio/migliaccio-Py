Alunni = [
    {"nome": "mario", "voti":{"matematica":6,"italino":6,"scienze":7,"inglese":4}},
    {"nome": "giovanni", "voti" : {"matematica": 4, "italino": 6, "scienze":5,"inglese":7,}},
    {"nome": "paola","voti":{"matematica":9,"italino":6, "scienze":8,"inglese":8}},
]

for i in Alunni:
    nome = i["nome"]
    media = sum(i["voti"].values()) / len(i["voti"])
    print(f"media dei voti di {nome} e di {media}")