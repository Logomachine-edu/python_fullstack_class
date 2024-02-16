def convert_to_hex(R, G, B):
    return "#{:02X}{:02X}{:02X}".format(R, G, B)
r_hex = convert_to_hex(255, 0, 0)
g_hex = convert_to_hex(0, 255, 0)
b_hex = convert_to_hex(0, 0, 255)

print(f"HEX: {r_hex}")
print(f"HEX: {g_hex}")
print(f"HEX: {b_hex}")