# PRINTING FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

import reports

def export(file_name):
    with open(file_name, "w") as f:
        f.write(str(reports.count_games("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.decide("game_stat.txt", "1997")))
        f.write("\n")
        f.write(str(reports.get_latest("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_by_genre("game_stat.txt", "RPG")))
        f.write("\n")
        f.write(str(reports.get_line_number_by_title("game_stat.txt", "Age of Empires")))

export("export.txt")
