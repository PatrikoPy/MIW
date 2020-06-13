students_list = [(147373, "Patryk Pe"), (146373, "Błażej Be"), (144373, "Wojtek Wu"), (137951, "Karol Ix"),
                 (147573, "Bartek Em")]
students_dict = {}
for student in students_list:
    students_dict[student[0]] = {"imie i nazwisko": student[1]}
for indeks in students_dict:
    students_dict[indeks].update({"wiek": 32})
    students_dict[indeks].update({"rok urodzenia": 1988})
    students_dict[indeks].update({"adres": "None"})
    students_dict[indeks].update({"email": "none@none.none"})

