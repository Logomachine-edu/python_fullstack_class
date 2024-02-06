def convert_units_with_while(units):
    unit = units[0]
    units_len = 0
    
    while units_len < len(unit):
        imp_unit = unit[units_len] * 3.28084
        print(f"{unit[units_len]} {units[1]}(s) = {imp_unit} foot(feet)")
        units_len += 1
        
convert_units_with_while(([1, 2], 'meter'))