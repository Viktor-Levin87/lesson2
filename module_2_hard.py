n = int(input('Введите число от 3 до 20: '))
pas = []
for i in range(1, 21):
    for j in range(1, 21):
        if i < j:
            if n % (i + j) == 0:
                pas.append(i)
                pas.append(j)
# print(''.join(map(str, pas)))
print('Пароль: ', *pas, sep='')
