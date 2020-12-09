import string

chars = "abcdefghijklmnopqrstuvwxyz"
chars_len = len(chars)
char_list = list(chars)
special = string.punctuation + " "


def rot_by_offset(text, offset):
    in_string = text.lower()
    in_list = list(in_string)
    start_ord = ord(char_list[0])
    end_ord = ord(char_list[-1])
    new_ord = 0
    out_string = ''

    for char in in_list:
        if char in special:
            new_ord = ord(char)
        else:
            char_ord = ord(char)
            wip_ord = char_ord + offset
            if  wip_ord > end_ord:
                r = wip_ord - end_ord
                new_ord = start_ord + (r - 1)
            else:
                new_ord = wip_ord
        out_string += chr(new_ord)

    return out_string


print(rot_by_offset("hello world!", 22))
print(rot_by_offset("uryyb jbeyq!", 4))

