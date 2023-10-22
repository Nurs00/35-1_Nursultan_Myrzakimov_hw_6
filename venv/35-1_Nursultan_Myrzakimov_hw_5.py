from decouple import config
from random import randint

initial_money = float(config('MY_MONEY'))

while initial_money > 0:
    print(f"Ваш текущий капитал: ${initial_money}")
    bet = float(input("Сделайте ставку: $"))

    if bet > initial_money:
        print("Ставка не может превышать ваш текущий капитал.")
    continue

    winning_slot = random(1,30)
    player_slot = int(input("Выберите слот от 1 до 30: "))

    if player_slot == winning_slot:
        initial_money += bet
        print(f"Поздравляем, вы выиграли ${bet}! Ваш текущий капитал: ${initial_money}")
    else:
        initial_money -= bet
        print(f"К сожалению, вы проиграли ${bet}. Ваш текущий капитал: ${initial_money}")

print("Игра окончена. Ваш капитал исчерпан.")