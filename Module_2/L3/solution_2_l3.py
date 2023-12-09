staff = 'Маша', 'Света', 'Паша', 'Олег'
even = staff[1::2]
odd = staff[::2]
even_d = " ".join(even)
odd_d = " ".join(odd)
print('В четные дни работают:', even_d, '\n \n' 'В нечетные дни работают:', odd_d)
