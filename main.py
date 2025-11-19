import random
from typing import List, Sequence, Any

## RANDOM NUMBER ##
def generate_random_with_user_range():
    print("--- Random Number Generator ---", flush=True)
    while True:
        try:
            min_limit = int(input("Enter the lower limit (minimum, e.g., 1): ").strip())
            break
        except ValueError:
            print("Error! Please enter a valid integer.", flush=True)

    while True:
        try:
            max_limit = int(input("Enter the upper limit (maximum, e.g., 100): ").strip())
            if max_limit < min_limit:
                print("Error! The upper limit must be greater than or equal to the lower limit.", flush=True)
            else:
                break
        except ValueError:
            print("Error! Please enter a valid integer.", flush=True)

    random_number = random.randint(min_limit, max_limit)
    print(f"\nThe random number generated between {min_limit} and {max_limit} is: **{random_number}**", flush=True)


##### SELECT FROM LIST #####
def rand_list(user_list: List[Any], percentages: Sequence[float]) -> Any:
    if len(user_list) != len(percentages):
        return "The list and the amount of percentages do not match. Please make them the same size."

    random_numbers = []

    for x in range(len(user_list)):
        num = random.randint(1, 100)
        random_numbers.append(num * percentages[x])

    winner_index = random_numbers.index(max(random_numbers))
    return user_list[winner_index]


# RANDOM_RANGE
def rand_range(min_range: float, max_range: float, true_min: float, true_max: float) -> Any:
    subtle_difference_number = random.randint(-3, 3)
    subtle_difference_number_1 = random.randint(-3, 3)

    true_max += subtle_difference_number
    true_min += subtle_difference_number_1

    while true_max > max_range:
        true_max -= 1

    while true_min < min_range:
        true_min += 1

    while true_min > max_range:
        true_min -= 1

    while true_max < min_range:
        true_max += 1

    while true_min > true_max:
        true_min -= random.randint(1, 3)

    return (true_min, true_max)


##### GENERAL INPUT #####
def general_input():
    while True:
        print("\n===== RANDOM GENERATOR PROJECT =====", flush=True)
        print("Tasks:", flush=True)
        print("1. Coin Flip  (Iván)", flush=True)
        print("2. Random Number (Kevin)", flush=True)
        print("3. Choose From List (Héctor)", flush=True)
        print("4. Random Range (Iván)", flush=True)
        print("0. Exit", flush=True)

        option = input("Select an option: ").strip()

        if option == "0":
            print("Exiting...", flush=True)
            break

        elif option == "1":
            print("\n-- Coin Flip (Iván) --", flush=True)
            result = random.choice(["Heads", "Tails"])
            print("Result:", result, flush=True)

        elif option == "2":
            generate_random_with_user_range()

        elif option == "3":
            print("\n-- Choose From List (Héctor) --", flush=True)
            raw_list = input("Enter the options separated by commas: ").strip()
            user_list = [item.strip() for item in raw_list.split(",")]

            raw_percentages = input("Enter the percentages (comma-separated, numbers 0-100): ").strip()
            try:
                percentages = [float(item.strip()) for item in raw_percentages.split(",")]
            except ValueError:
                print("Error: percentages must be numbers.", flush=True)
                continue

            result = rand_list(user_list, percentages)
            print("\nResult:", result, flush=True)

        elif option == "4":
            print("\n-- Random Range (Kevin) --", flush=True)
            try:
                min_range = float(input("Enter min_range: ").strip())
                max_range = float(input("Enter max_range: ").strip())
                true_min = float(input("Enter true_min: ").strip())
                true_max = float(input("Enter true_max: ").strip())
                print("\nGenerated range:", rand_range(min_range, max_range, true_min, true_max), flush=True)
            except ValueError:
                print("Error: invalid input. Use numbers.", flush=True)

        else:
            print("Invalid option. Try again.", flush=True)


##### RUN PROGRAM #####
if __name__ == "__main__":
    general_input()

