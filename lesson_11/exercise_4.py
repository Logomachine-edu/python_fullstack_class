def convert_units_with_while(unit_list, unit_list_m):
    total = 0
    while len(unit_list) > total:
        print(f"{unit_list[total]} {unit_list_m}(s) = {unit_list[total] * 3.28084} foot(feet)")
        total += 1


convert_units_with_while([1, 2], 'meter')
