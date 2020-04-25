def remove_letter(text, letter):
    while (letter in text):
        text = text.replace(letter, "")
    return text


print(remove_letter(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "it"))
