def analyze_ad_efficiency(clicks, impressions, views):
    ratio = clicks / impressions
    if ratio < 0.01 and views > impressions:
        print("Недооцененная")
    elif 0.01 and ratio < 0.05 and views:
        print('Низкая')
    elif 0.05 and ratio < 0.1 and views > clicks:
        print('Средняя')
    elif ratio >= 0.1 and views:
        print('Высокая')
    else:
        print('Неопределенная')


analyze_ad_efficiency(50, 10000, 15000)
analyze_ad_efficiency(200, 10000, 5000)
analyze_ad_efficiency(700, 10000, 800)
analyze_ad_efficiency(1200, 10000, 1000)
analyze_ad_efficiency(500, 10000, 200)
