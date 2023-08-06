def letters_len(input_var):
    letter = 0
    for i in input_var:
        if i.isalpha():
            letter += 1
    return letter


def revers_string(b):
    return b[::-1]


if __name__ == "__main__":
    print(revers_string('dota2'))
    print(letters_len('wow1'))
