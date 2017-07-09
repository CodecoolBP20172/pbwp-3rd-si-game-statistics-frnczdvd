# PRINTING FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

import reports

def printing():
    print("")
    print("Judy's questions (part 2):")
    print("1. What is the title of the most played game?     ", reports.get_most_played("game_stat.txt"))
    print("2. How many copies have been sold total?          ", reports.sum_sold("game_stat.txt"))
    print("3. What is the average selling?                   ", reports.get_selling_avg("game_stat.txt"))
    print("4. How many characters long is the longest title? ", reports.count_longest_title("game_stat.txt"))
    print("5. What is the average of the release dates?      ", reports.get_date_avg("game_stat.txt"))
    print("6. What properties has a game?                    ", reports.get_game("game_stat.txt", "Age of Empires"))
    print("")
printing()