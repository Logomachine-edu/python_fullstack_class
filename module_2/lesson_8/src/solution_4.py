design = {}
supply = {}
i : int = 0

while i < 6:
    general_input = list(input("Введите отдел, должность и фамилию через запятую:").lower().split(','))
    
    if general_input[0] == "снабжение":
            supply[general_input[1]] = general_input[2]
    else:
            if general_input[0] == "дизайн":
                design[general_input[1]] = general_input[2]
            else:
                  print("Работник не относится к интересующим разделам!")

    i = i+1


print("Снабжение:" , supply , "Дизайн:" , design)    