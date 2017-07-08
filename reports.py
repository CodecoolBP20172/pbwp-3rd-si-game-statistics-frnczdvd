# REPORT FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

def count_games(file_name):
    count = 0
    try:
        with open(file_name) as f:
            for line in f:
                count += 1
        return count
    except FileNotFoundError:
        return "File not found"
        
def decide(file_name, year):
    try:
        with open(file_name) as f:
            for line in f:
                if year in line:
                    return True
        return False
    except FileNotFoundError:
        return "File not found"

def get_latest(file_name):
    count1 = 0
    count2 = str()
    try:
        with open(file_name) as f:
            for line in f:
                year = int(line.split("\t")[2])
                title = line.split("\t")[0]
                if year > count1:
                    count1 = year
                    count2 = title
            return (count2)
    except FileNotFoundError:
        return "File not found"

def count_by_genre(file_name, genre):
    count = 0
    try:
        with open(file_name) as f:
            for line in f:
                if genre == line.split("\t")[3]:
                    count += 1
        return count
    except FileNotFoundError:
        return "File not found"

def get_line_number_by_title(file_name, title):
    count = 0
    try:
        with open(file_name) as f:
            for line in f:
                count += 1
                if title == line.split("\t")[0]:
                    return count
        raise ValueError("Game not found")
    except FileNotFoundError:
        return "File not found"
