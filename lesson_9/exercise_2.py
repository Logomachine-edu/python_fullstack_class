def convert_to_hex(rgb):
    hexadecimal = f"#{format(rgb[0], '02X')}{format(rgb[1], '02X')}{format(rgb[2], '02X')}"
    print(f"Hex: {hexadecimal}")


convert_to_hex([255, 0, 0])
convert_to_hex([0, 255, 0])
convert_to_hex([0, 0, 255])
