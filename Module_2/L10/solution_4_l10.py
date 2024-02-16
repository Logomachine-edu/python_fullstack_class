def choose_ad_platform(budget):
    
    
    if budget > 5000:
        print('Instagram')
    elif 1000 <= budget < 5000:
        print('Facebook')
    else:
        print('Google')

choose_ad_platform(500)
choose_ad_platform(3000)
choose_ad_platform(6000)