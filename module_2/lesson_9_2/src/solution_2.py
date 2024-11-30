RGB = list(map(int, input('RGB: ').split(',')))
def convert_to_hex(RGB):
    translation_R = format(RGB[0], '02X')
    translation_G = format(RGB[1], '02X')
    translation_B = format(RGB[2], '02X')
    full_translation = str(translation_R) + str(translation_G) + str(translation_B)
    return full_translation
print(f"HEX: {convert_to_hex(RGB)}")