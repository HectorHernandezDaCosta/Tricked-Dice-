import random
from typing import List, Sequence, Any


##RANDOM NUMBER##

def generate_random_with_user_range():
  print("--- Random Number Generator ---")
  # 1. Ask the user for the minimum limit
  while True:
    try:
      min_limit = int(input("Enter the lower limit (minimum, e.g., 1): "))
      break
    except ValueError:
      print("Error! Please enter a valid integer.")
  # 2. Ask the user for the maximum limit
  while True:
    try:
      max_limit = int(input("Enter the upper limit (maximum, e.g., 100): "))
      if max_limit < min_limit:
        print("Error! The upper limit must be greater than or equal to the lower limit.")
      else:
        break
    except ValueError:
      print("Error! Please enter a valid integer.")
  # 3. Generate the random number
  random_number = random.randint(min_limit, max_limit)
  # 4. Display the result
  print(f"\n The random number generated between {min_limit} and {max_limit} is: **{random_number}**")
generate_random_with_user_range()


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




##### GENERAL INPUT #####

def general_input():
    while True:
        print("\n===== RANDOM GENERATOR PROJECT =====")
        print("Tasks:")
        print("1. Coin Flip (Iván)")
        print("2. Random Number (Kevin)")
        print("3. Choose From List (Héctor)")
        print("0. Exit")
        option = input("Select an option: ")

        if option == "0":
            print("Exiting...")
            break

        elif option == "1":
            print("\n-- Coin Flip (Iván) --")
            print("Feature not implemented yet by Iván.")

        elif option == "2":
            generate_random_with_user_range()

        elif option == "3":
            print("\n-- Choose From List (Héctor) --")
            raw_list = input("Enter the options separated by commas: ")
            user_list = [item.strip() for item in raw_list.split(",")]

            raw_percentages = input("Enter the percentages (comma-separated): ")
            percentages = [float(item.strip()) for item in raw_percentages.split(",")]

            result = rand_list(user_list, percentages)
            print("\nResult:", result)

        else:
            print("Invalid option. Try again.")


##### RUN #####

if __name__ == "__main__":
    general_input()

