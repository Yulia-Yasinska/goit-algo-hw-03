import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity <= 0:
        print("Введіть min, max та quantity у заданих обмеженнях!")
        return None
    lottery_list = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_list)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)