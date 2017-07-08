# PRINTING FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

import reports

def printing():
    print("")
    print("Judy's questions:")
    print("1. How many games are in the file?               ", reports.count_games("game_stat.txt"))
    print("2. Is there a game from 1997?                    ", reports.decide("game_stat.txt", "1997"))
    print("3. Which was the latest game?                    ", reports.get_latest("game_stat.txt"))
    print("4. How many RPG games do we have?                ", reports.count_by_genre("game_stat.txt", "RPG"))
    print("5. What is the line number of Age of Empires?    ", reports.get_line_number_by_title("game_stat.txt", "Age of Empires"))
    print("")
printing()