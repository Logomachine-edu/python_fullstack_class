category = [1, 2, 3, 4]
category_numbers = [int(x) for x in category]


def convert_units_with_while(lst , system = "meters"):
  i = 0
  if system == "meters":
    while i < len(lst):
      print(f"{lst[i]} {system} = {lst[i] * 3.28084} foot(feets)")
      i += 1
  else: print("Данной системы пока не заложено =(")

convert_units_with_while(category_numbers)