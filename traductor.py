def binary_to_decimal(binary):
    return int(str("0b"+binary), 2)


def decimal_to_binary(num):
    return bin(num).replace("0b", "")


def bin_to_text(binary):
    binary_string = ''
    text = ''

    for i in binary:
        # Anything is not a 0, 1 or an space, gets discarded
        if i == '0' or i == '1' or i == ' ':
            binary_string += i

    binary_split = binary_string.split(' ')
    code = []

    # Gets the ASCII char converting the binary to his decimal value
    for i in binary_split:
        char = binary_to_decimal(i)
        code.append(chr(char))
    text = ('').join(code)
    return text


def text_to_bin(text):
    text_split = list(text)
    code = []
    for i in text_split:
        code.append(decimal_to_binary(ord(i)))
        code.append(" ")
    return "".join(code)
