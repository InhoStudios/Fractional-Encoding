def construct_decimal_string_from_text(text):
    # use 0-127 for character encoding
    char_string = "0."
    for char in text:
        char_value = str(ord(char)).zfill(3)
        char_string = char_string + char_value
    return char_string


if (__name__ == "__main__"):
    print(construct_decimal_string_from_text("Hello world!"))