dict_list = [{"indeks": 147373, "student": 'Patryk Pe', "wynik": 4.5},
             {"indeks": 147951, "student": 'Błażej Be', "wynik": 3.5},
             {"indeks": 147873, "student": 'Wojtek Wu', "wynik": 4.0},
             {"indeks": 147159, "student": 'Karol Ix', "wynik": 3.0},
             {"indeks": 147378, "student": 'Bartek Em', "wynik": 5.0}]

for dict in dict_list:
    print("Student: {:.>40}, nr indeksu:{:.>10}\twynik: {:3.2f}".format(dict["student"],dict["indeks"],dict["wynik"]))
