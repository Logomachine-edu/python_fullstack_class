rgb = tuple(input("Введите 3 числа цвета RGB через запятую:").split(","))
rgb_numbers = [int(x) for x in rgb]

def convert_to_hex (*args) -> str:     
    red = hex(rgb_numbers[0])[2::]
    green = hex(rgb_numbers[1])[2::]
    blue = hex(rgb_numbers[2])[2::]
    return red+green+blue

print(convert_to_hex(rgb_numbers))