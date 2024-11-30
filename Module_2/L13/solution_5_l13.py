def authorization(authorization_data):
    def wrapper(username, password):
        if username == 'Роман' and password == 'correctpassword':
            print('Доступ получен. Данные: ...')
        else:
            print('В доступе отказано!')
    return wrapper

@authorization
def access_client_data() -> None:
    pass
    
authorization_data = [    
    access_client_data('Роман', 'correctpassword'),
    access_client_data('Олег', 'wrongpassword')
]