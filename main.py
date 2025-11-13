import random
from typing import List, Sequence, Any






#####SELECT FROM LIST#####

def rand_list(user_list: List[Any], percentages: Sequence[float]) -> Any:
#Check if the list of user options is the same lenght as the one with the percentages
    if len(user_list) != len(percentages):
        return "The list and the amount of percentages do not match. Please make them the same size."

    random_numbers = []

#Assing random number to each option in a  new array
    for x in range(len(user_list)):
        num = random.randint(1, 100)
        random_numbers.append(num * percentages[x])

    winner_index = random_numbers.index(max(random_numbers))
    return user_list[winner_index]

#Example
#print(rand_list(["Max", "jhon", "sophie"], (10, 70, 3)))
