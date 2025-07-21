import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity <= 0 or max < min or quantity > max - min:
        print("Введіть коректні min, max та quantity!")
        return []
    lottery_list = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_list)

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)