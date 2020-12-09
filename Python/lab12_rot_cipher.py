import string




def rot_by_offset(text, offset):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars_len = len(chars)
    char_list = list(chars)
    special = string.punctuation + " "

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
            if  offset > 0 and wip_ord > end_ord:
                r = wip_ord - end_ord
                new_ord = start_ord + (r - 1)
            elif offset < 0 and wip_ord < start_ord:
                r = start_ord - wip_ord
                new_ord = end_ord - (r - 1)
            else:
                new_ord = wip_ord
        out_string += chr(new_ord)

    return out_string
    



def rot_all_characters_by_offset(chars, offset):
    encoder = string.ascii_letters + string.punctuation + " "

    encoder_len = len(encoder)
    encoder_list = list(encoder)

    encoder_dict_index = {}
    for i in range(len(encoder_list)):
        encoder_dict_index[encoder_list[i]] = i
    
    encoder_dict_char = {}
    for i in range(len(encoder_list)):
        encoder_dict_char[i] = encoder_list[i]

    chars_list = list(chars)
    start_ord = encoder[0]
    end_ord = encoder[-1]
    new_ord = 0
    out_string = ''

    for char in chars_list:
        if not (char in encoder):
            new_ord = encoder_dict_index[char]
        else:
            char_ord = encoder_dict_index[char]
            wip_ord = char_ord + offset
            if  offset > 0 and wip_ord > encoder_dict_index[end_ord]:
                r = wip_ord - encoder_dict_index[end_ord]
                new_ord = encoder_dict_index[start_ord] + (r - 1)

            elif  offset < 0 and wip_ord < encoder_dict_index[start_ord]:
                r = encoder_dict_index[start_ord] - wip_ord
                new_ord = encoder_dict_index[end_ord] - (r - 1)
            else:
                new_ord = wip_ord
        out_string += encoder_dict_char[new_ord]
    return out_string

offset = 22
output = rot_by_offset("hello world!", offset)
print(output)
output = rot_by_offset(output, (-1 * offset))
print(output)


offset = 2
output = rot_all_characters_by_offset(output, offset)
print(output)

output = rot_all_characters_by_offset(output, (-1 * offset))
print(output)


