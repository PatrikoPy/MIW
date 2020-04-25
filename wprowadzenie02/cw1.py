def join_two_list(a_list, b_list):
    return a_list[1::2] + b_list[0::2]


print(join_two_list([1, 2, 3, 4, 5], ["pierwszy", "drugi", "trzeci", "czwarty", "piąty"]))
