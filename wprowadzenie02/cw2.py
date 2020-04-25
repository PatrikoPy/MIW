def text_dict(data_text):
    dict = {}
    dict.update(length=len(data_text), letters=[letter for letter in data_text if letter.isalnum()],
                big_letters=data_text.upper(),
                small_letters=data_text.lower())
    return dict


if __name__ == "__main__":
    print(text_dict("New Text.name2"))
