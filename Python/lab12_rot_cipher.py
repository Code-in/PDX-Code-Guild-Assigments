import string
import random



# ROT encoder which only supports lowercase ASCII characters
def rot_by_offset(text, offset):

    # Set up our supported encoder characters as a string
    chars = "abcdefghijklmnopqrstuvwxyz"

    # Convert the encoder string to a list
    char_list = list(chars)

    # set up boundry check arguements
    in_string = text.lower()
    in_list = list(in_string)
    start_ord = ord(char_list[0])
    end_ord = ord(char_list[-1])
    new_ord = 0
    output = ''

    # loop throught the incomin data to encode
    for char in in_list:
        if not (char in chars):
            new_ord = ord(char)
        else:
            char_ord = ord(char)
            wip_ord = char_ord + offset
            # Check for positive offset for the encoding then handle length and wrap around to the beginnning
            if  offset > 0 and wip_ord > end_ord:
                r = wip_ord - end_ord
                new_ord = start_ord + (r - 1)
            # Check for negative offsets for the encoding then handle length and wrap around to the beginnning
            elif offset < 0 and wip_ord < start_ord:
                r = start_ord - wip_ord
                new_ord = end_ord - (r - 1)
            # All conditions not met by the conditionals above we need to with new offset character
            else:
                new_ord = wip_ord
        # append the output char to the output string
        output += chr(new_ord)
    # return final output string
    return output
    


# ROT encoder with a larger character set which supports all ASCII characters and punctation
def rot_all_characters_by_offset(chars, offset):

    # Set up our supported encoder characters as a string
    encoder = string.ascii_letters + string.punctuation + " "

    # Convert the encoder string to a list
    encoder_list = list(encoder)

    # Dictionary with keys as chars and values at int
    encoder_dict_index = {}
    for i in range(len(encoder_list)):
        encoder_dict_index[encoder_list[i]] = i
    
    # Dictionary with keys as int(index values) and values as chars
    encoder_dict_char = {}
    for i in range(len(encoder_list)):
        encoder_dict_char[i] = encoder_list[i]

    # set up boundry check arguements
    chars_list = list(chars)
    start_char = encoder[0]
    end_char = encoder[-1]
    new_char_index = 0
    output = ''

    # loop throught the incomin data to encode
    for char in chars_list:
        # if character not in the encoder set skip encode that character
        if char not in encoder:
            new_char_index = encoder_dict_index[char]
        else:
            char_index = encoder_dict_index[char]
            wip_ord = char_index + offset
            # Check for positive offset for the encoding then handle length and wrap around to the beginnning
            if  offset > 0 and wip_ord > encoder_dict_index[end_char]:
                r = wip_ord - encoder_dict_index[end_char]
                new_char_index = encoder_dict_index[start_char] + (r - 1)

            # Check for negative offsets for the encoding then handle length and wrap around to the beginnning
            elif  offset < 0 and wip_ord < encoder_dict_index[start_char]:
                r = encoder_dict_index[start_char] - wip_ord
                new_char_index = encoder_dict_index[end_char] - (r - 1)
            # All conditions not met by the conditionals above we need to with new offset character
            else:
                new_char_index = wip_ord
        # append the output char to the output string
        output += encoder_dict_char[new_char_index]
    
    # return final output string
    return output



offset = 13
in_output = "hello world"
output = rot_by_offset(in_output, offset)
print(output)
output = rot_by_offset(output, (-1 * offset))
print(output)

offset = random.randint(0, 25)
in_output = "hello world!@&$^#(#"
output = rot_by_offset(in_output, offset)
print(output)
output = rot_by_offset(output, (-1 * offset))
print(output)

offset = random.randint(0, 84)
output = rot_all_characters_by_offset(output, offset)
print(output)
out_output = rot_all_characters_by_offset(output, (-1 * offset))
print(out_output)

if in_output == out_output:
    print("Successes!!!!")
else:
    print("FAILURE")



