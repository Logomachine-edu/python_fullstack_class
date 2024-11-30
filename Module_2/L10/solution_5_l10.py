def analyze_ad_efficiency(clicks, impressions, views):
    
    
    if clicks / impressions < 0.01 and impressions < views:
        print('Недооцененная')
    elif 0.01 < clicks / impressions < 0.05:
        print('Низкая')
    elif 0.05 < clicks / impressions < 0.1 and clicks < views:
        print('Средняя')
    elif clicks / impressions > 0.1:
        print('Высокая')
    else:
        print('Неопределенная')
        
analyze_ad_efficiency(50, 10000, 15000)
analyze_ad_efficiency(200, 10000, 5000)
analyze_ad_efficiency(700, 10000, 800)
analyze_ad_efficiency(1200, 10000, 1000)
analyze_ad_efficiency(500, 10000, 200)