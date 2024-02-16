def background_time(time):
    
    
    if 6 <= time < 18:
      print('Цвет фона: Светлый')
    elif 18 <= time <= 23 or 0 <= time < 6:
      print('Цвет фона: Темный')
    
background_time(10)
background_time(20)
background_time(5)