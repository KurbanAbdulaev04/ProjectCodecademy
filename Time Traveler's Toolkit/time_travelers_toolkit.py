import datetime as dt

from decimal import Decimal
from random import choice
from random import randint
from custom_module import generate_time_travel_message

print(dt.date.today(), dt.datetime.now().time())

current_year = dt.datetime.now().year

random_year = randint(500, 3000)

base_cost = Decimal('1500.00')
year_difference = abs(current_year - random_year)

cost_multiplier = Decimal('13.00') * Decimal(year_difference)
final_cost = base_cost + cost_multiplier

final_cost = round(final_cost, 2)
print(f"Final cost: ${final_cost}")

random_year = randint(500, 3000)

list_one = ['A','B','C','D']
list_one = choice(list_one)

print(generate_time_travel_message(random_year, list_one, final_cost))