import random as r
print("Вы вошли в игру в *Кости*, у тебя есть немного монеток!")
print("Ты и крупье ставите ставки. Выбираете числа от 1 до 6(по 3 числа каждый).У всех по 10 долларов")
my_money = 10
croupier_money = 10


def stavka(user_money, croupier_money):
    user_stavka = int(input('Сколько вы готовы поставить?'))
    if user_stavka > user_money:
        print('Недостаточно средств!')
    croupier_stavka = r.randint(1, croupier_money)
    while croupier_stavka != user_stavka:
        croupier_stavka = r.randint(1, croupier_money)
    print('Крупье ставит: ', croupier_stavka)
    user_money -= user_stavka
    croupier_money -= croupier_stavka
    stavki = [user_stavka, croupier_stavka]
    return stavki


def randomizer():
    a = [1, 2, 3, 4, 5, 6]
    croup = []
    player = []
    for i in range(3):
        b = r.choice(a)
        b = a.index(b)
        player.append(a.pop(b))
    for i in range(3):
        b = r.choice(a)
        b = a.index(b)
        croup.append(a.pop(b))
    mass = list()
    mass.append(player)
    mass.append(croup)
    return mass


def base(user_money, croupier_money):
    if user_money == 0 or croupier_money == 0:
        print('Игра закончена, у кого-то из вас закончились деньги!')
        return
    print('У вас есть', user_money)
    print('У крупье есть', croupier_money)
    stavki = stavka(my_money, croupier_money)
    croupier_stavka = stavki[1]
    user_stavka = stavki[0]
    first_move = r.randint(1, 2)
    if first_move == 1:
        print("Ты выбираешь первый")
        m = input("Ты готов кинуть кости? Что-бы узнать какие числа выпадут тебе")
        if m == "Да" or "Lf":
            my_n = randomizer()
            croupier_n = my_n[1]
            my_n = my_n[0]
            print("Твои числа : ", my_n)
            print("Теперь крупье кидает кубик")
            print("Иии ему выпали числа : ", croupier_n)
    else:
        print("Крупье выбирает первый")
        croupier_n = randomizer()
        my_n = croupier_n[1]
        croupier_n = croupier_n[0]
        print("Крупье выбрал: ", croupier_n)

        j = input("Ты готов кинуть кости? Что-бы узнать какие числа выпадут тебе")
        if j == "Да" or "Lf":
            print("Твои числа : ", my_n)

    dice = r.randint(1, 6)
    print('Трясём кубик, чтобы узнать, кто победил...')
    print('Ещё немного...')
    print('На кубике светится число:', dice)
    if dice in my_n:
        print('Победил игрок! Поздравляем!')
        user_money += croupier_stavka
        croupier_money -= croupier_stavka
        print('Вы выиграли', croupier_stavka, 'долларов!')
    else:
        print('Победил крупье! Поздравляем!')
        croupier_money += user_stavka
        user_money -= user_stavka
        print('Крупье выиграл', user_stavka, 'долларов!')
    h = input("Не против сыграть ещё?")
    if h == "lf" or "да":
        base(user_money, croupier_money)
    else:
        print("Прощай!")


base(my_money, croupier_money)

