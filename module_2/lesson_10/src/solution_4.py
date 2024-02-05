budget = int(input("Введите ваш бюджет:"))

def choose_ad_platform(a):
    if a < 1000 : 
        result = "Google"
    elif 1000 <= a <= 5000:
        result = "Facebook"
    else:
        result = "Instagram"
    
    return result

print("Вам подходит компания:", choose_ad_platform(budget))