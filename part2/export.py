# EXPORT FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

import reports

def export(file_name):
    with open(file_name, "w") as f:
        f.write(str(reports.get_most_played("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.sum_sold("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_selling_avg("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.count_longest_title("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_date_avg("game_stat.txt")))
        f.write("\n")
        f.write(str(reports.get_game("game_stat.txt", "Age of Empires")))
export("export.txt")
