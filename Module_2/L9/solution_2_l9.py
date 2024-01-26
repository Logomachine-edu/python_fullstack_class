numbers = list(map(int, input('RGB: ').split(", ")))

def convert_to_hex(numbers):
    num_hex = f'#{numbers[0]:02X}{numbers[1]:02X}{numbers[2]:02X}'
    return num_hex
    
hex_numbers = convert_to_hex(numbers)
print(f"HEX: {hex_numbers}")